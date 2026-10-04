#!/usr/bin/env python3
"""
AST fingerprinting using tree edit distance and structural similarity.
Implements Zhang-Shasha tree edit distance algorithm for accurate AST comparison.
"""

import hashlib
import os
import logging
import numpy as np
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict, Counter
from dataclasses import dataclass, field
from functools import lru_cache
from tools.parser_libclang import ASTNode

# Global cache for tree edit distance computations
_ted_cache: Dict[Tuple[int, int], int] = {}


@dataclass
class ASTFingerprint:
    """
    Multi-level fingerprint for similarity-preserving AST comparison.
    Does not rely on hashing for similarity - uses structural features.
    """
    # Level 1: Ordered sequence of node types (preserves structure)
    node_sequence: List[str] = field(default_factory=list)
    
    # Level 2: Subtree patterns (for overlap detection)
    subtree_patterns: Set[str] = field(default_factory=set)
    
    # Level 3: Statistical features
    depth: int = 0
    size: int = 0  # Number of nodes
    feature_vector: Dict[str, int] = field(default_factory=dict)  # Node type frequencies
    
    # Original AST reference for tree edit distance computation
    ast_node: Optional[ASTNode] = None
    
    def similarity(self, other: 'ASTFingerprint') -> float:
        """
        Compute similarity score (0.0-1.0) using tree edit distance and Jaccard.
        Optimized with caching and smart pre-filtering for speed.
        """
        if self.ast_node is None or other.ast_node is None:
            return self._fallback_similarity(other)
        
        # Quick check: if same object, return 1.0
        if self.ast_node is other.ast_node:
            return 1.0
        
        # Quick Jaccard pre-filter: only skip TED for very dissimilar trees
        jaccard = self._jaccard_similarity(other)
        if jaccard < 0.3:  # Only skip TED when patterns are very different
            return 0.3 * jaccard  # Pessimistic estimate
        
        # Compute cached tree edit distance for similar trees only
        tree_distance = tree_edit_distance_cached(self.ast_node, other.ast_node)
        max_size = max(self.size, other.size)
        tree_sim = 1.0 - (tree_distance / max_size) if max_size > 0 else 0.0
        
        # Weighted combination: 70% tree edit distance (structural), 30% Jaccard (patterns)
        return 0.70 * tree_sim + 0.30 * jaccard
    
    def _fallback_similarity(self, other: 'ASTFingerprint') -> float:
        """Fallback similarity when AST nodes are not available - use only subtree patterns."""
        # Only Jaccard similarity when tree edit distance is unavailable
        return self._jaccard_similarity(other)
    
    def _jaccard_similarity(self, other: 'ASTFingerprint') -> float:
        """Jaccard similarity on subtree patterns."""
        if not self.subtree_patterns and not other.subtree_patterns:
            return 1.0
        
        intersection = len(self.subtree_patterns & other.subtree_patterns)
        union = len(self.subtree_patterns | other.subtree_patterns)
        
        return intersection / union if union > 0 else 0.0


@dataclass
class Fragment:
    """Code fragment with metadata."""
    prog_id: str
    clause_id: str
    fragment_id: str
    ast: ASTNode
    code_snippet: str
    fingerprint: ASTFingerprint  # Now uses ASTFingerprint instead of hash string
    position: int  # Position in original code


def levenshtein_distance(seq1: List[str], seq2: List[str]) -> int:
    """
    Compute Levenshtein (edit) distance between two sequences.
    Uses dynamic programming for efficiency.
    """
    if seq1 == seq2:
        return 0
    if len(seq1) == 0:
        return len(seq2)
    if len(seq2) == 0:
        return len(seq1)
    
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i-1] == seq2[j-1]:
                cost = 0
            else:
                cost = 1
            
            dp[i][j] = min(
                dp[i-1][j] + 1,      # deletion
                dp[i][j-1] + 1,      # insertion
                dp[i-1][j-1] + cost  # substitution
            )
    
    return dp[m][n]


def _get_node_id(node: ASTNode) -> int:
    """Get unique ID for AST node for caching."""
    return id(node)


def tree_edit_distance_cached(tree1: ASTNode, tree2: ASTNode) -> int:
    """
    Cached wrapper for tree edit distance computation.
    Uses global cache to avoid recomputing same tree pairs.
    """
    if tree1 is None and tree2 is None:
        return 0
    if tree1 is None:
        return _count_nodes(tree2)
    if tree2 is None:
        return _count_nodes(tree1)
    
    # Check cache
    node1_id = _get_node_id(tree1)
    node2_id = _get_node_id(tree2)
    cache_key = (min(node1_id, node2_id), max(node1_id, node2_id))
    
    if cache_key in _ted_cache:
        return _ted_cache[cache_key]
    
    # Compute and cache
    distance = tree_edit_distance(tree1, tree2)
    _ted_cache[cache_key] = distance
    return distance


def tree_edit_distance(tree1: ASTNode, tree2: ASTNode) -> int:
    """
    Compute tree edit distance using Zhang-Shasha algorithm.
    Optimized with early termination for small trees and size bounds.
    
    Operations:
    - Delete a node
    - Insert a node
    - Relabel a node
    
    Returns: Minimum number of operations to transform tree1 into tree2
    """
    if tree1 is None and tree2 is None:
        return 0
    if tree1 is None:
        return _count_nodes(tree2)
    if tree2 is None:
        return _count_nodes(tree1)
    
    # Quick check: if roots are equal and both are leaves, distance is 0
    if _nodes_equal(tree1, tree2) and not tree1.children and not tree2.children:
        return 0
    
    # Size limit: skip tree edit distance for large trees (use upper bound estimate)
    size1 = _count_nodes(tree1)
    size2 = _count_nodes(tree2)
    max_nodes_env = os.getenv("AST_MERGE_MAX_NODES")
    try:
        max_nodes = int(max_nodes_env) if max_nodes_env else 200
    except ValueError:
        max_nodes = 200
    if size1 > max_nodes or size2 > max_nodes:  # Size limit for edit distance
        # Return upper bound: max of two tree sizes
        return max(size1, size2)
    
    # Build keyroot and left-most leaf mappings for both trees
    keyroots1, lmld1 = _compute_keyroots_and_lmld(tree1)
    keyroots2, lmld2 = _compute_keyroots_and_lmld(tree2)
    
    # Get post-order node lists
    nodes1 = _postorder_nodes(tree1)
    nodes2 = _postorder_nodes(tree2)
    
    n1 = len(nodes1)
    n2 = len(nodes2)
    
    # Tree distance matrix
    tree_dist = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    
    # Compute tree distances for all keyroot pairs
    for i in keyroots1:
        for j in keyroots2:
            forest_dist = [[0] * (n2 + 1) for _ in range(n1 + 1)]
            
            # Initialize forest distance
            for di in range(lmld1[i], i + 1):
                forest_dist[di][0] = forest_dist[di - 1][0] + 1
            for dj in range(lmld2[j], j + 1):
                forest_dist[0][dj] = forest_dist[0][dj - 1] + 1
            
            # Compute forest distances
            for di in range(lmld1[i], i + 1):
                for dj in range(lmld2[j], j + 1):
                    node1 = nodes1[di - 1]
                    node2 = nodes2[dj - 1]
                    
                    # Cost of relabeling
                    cost = 0 if _nodes_equal(node1, node2) else 1
                    
                    if lmld1[di] == lmld1[i] and lmld2[dj] == lmld2[j]:
                        # Both are trees
                        forest_dist[di][dj] = min(
                            forest_dist[di - 1][dj] + 1,           # delete from tree1
                            forest_dist[di][dj - 1] + 1,           # insert into tree1
                            forest_dist[di - 1][dj - 1] + cost     # relabel
                        )
                        tree_dist[di][dj] = forest_dist[di][dj]
                    else:
                        # At least one is a forest
                        forest_dist[di][dj] = min(
                            forest_dist[di - 1][dj] + 1,           # delete
                            forest_dist[di][dj - 1] + 1,           # insert
                            forest_dist[lmld1[di] - 1][lmld2[dj] - 1] + tree_dist[di][dj]
                        )
    
    return tree_dist[n1][n2]


def _count_nodes(node: ASTNode) -> int:
    """Count total number of nodes in tree."""
    if node is None:
        return 0
    count = 1
    for child in node.children:
        count += _count_nodes(child)
    return count


def _postorder_nodes(node: ASTNode) -> List[ASTNode]:
    """Get nodes in post-order traversal."""
    nodes = []
    
    def traverse(n):
        for child in n.children:
            traverse(child)
        nodes.append(n)
    
    traverse(node)
    return nodes


def _compute_keyroots_and_lmld(root: ASTNode) -> Tuple[List[int], Dict[int, int]]:
    """
    Compute keyroots and left-most leaf descendants for Zhang-Shasha.
    
    Returns:
        keyroots: List of keyroot indices (1-based)
        lmld: Dict mapping node index to left-most leaf descendant index (1-based)
    """
    nodes = _postorder_nodes(root)
    n = len(nodes)
    
    # Compute left-most leaf descendants (1-based indexing)
    lmld = {}
    for i, node in enumerate(nodes, start=1):
        if not node.children:
            lmld[i] = i
        else:
            # Find left-most child in post-order
            leftmost_child = node.children[0]
            leftmost_idx = nodes.index(leftmost_child) + 1
            lmld[i] = lmld[leftmost_idx]
    
    # Compute keyroots
    keyroots_set = set()
    for i in range(1, n + 1):
        l = lmld[i]
        if l not in keyroots_set:
            keyroots_set.add(l)
    
    # Root is always a keyroot
    keyroots_set.add(n)
    
    keyroots = sorted(keyroots_set)
    
    return keyroots, lmld


def _nodes_equal(node1: ASTNode, node2: ASTNode) -> bool:
    """
    Check if two nodes are equal (for tree edit distance).
    Uses normalized representation (ignores variable names).
    """
    if node1.kind != node2.kind:
        return False
    
    # For normalized comparison
    token1 = _normalize_token(node1)
    token2 = _normalize_token(node2)
    
    return token1 == token2


def _normalize_token(node: ASTNode) -> str:
    """Normalize token for comparison (same logic as before)."""
    if _is_identifier_like(node):
        return "ID"
    elif _is_literal(node):
        return "LIT"
    elif node.token and _should_keep_token(node, node.token):
        return node.token
    else:
        return ""


def _is_identifier_like(node: ASTNode) -> bool:
    """Check if node is an identifier or declaration."""
    identifier_kinds = {
        "DECL_REF_EXPR", "VAR_DECL", "PARM_DECL", "FUNCTION_DECL",
        "identifier", "field_identifier", "type_identifier",
        "UNEXPOSED_EXPR"
    }
    return node.kind in identifier_kinds


def _is_literal(node: ASTNode) -> bool:
    """Check if node is a literal value."""
    literal_kinds = {
        "INTEGER_LITERAL", "FLOATING_LITERAL", "STRING_LITERAL",
        "CHARACTER_LITERAL", "number_literal", "string_literal",
        "char_literal"
    }
    return node.kind in literal_kinds


def _should_keep_token(node: ASTNode, token: str) -> bool:
    """Determine if a token should be preserved."""
    if not token:
        return False
    
    operators = {
        '+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=',
        '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', 
        '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=',
        '++', '--', '->', '.', '?', ':'
    }
    if token in operators:
        return True
    
    keywords = {
        'if', 'else', 'while', 'for', 'do', 'switch', 'case', 'default',
        'break', 'continue', 'return', 'goto', 'sizeof', 'typeof'
    }
    if token in keywords:
        return True
    
    stdlib_funcs = {
        'printf', 'scanf', 'malloc', 'free', 'memcpy', 'memset',
        'strlen', 'strcmp', 'strcpy', 'fopen', 'fclose', 'fread', 'fwrite',
        'abs', 'sqrt', 'pow', 'sin', 'cos', 'modf', 'floor', 'ceil'
    }
    if token in stdlib_funcs:
        return True
    
    return False


class Fingerprinter:
    """Computes multi-level fingerprints for AST subtrees using structural similarity."""
    
    def __init__(self):
        self.logger = logging.getLogger("ast_merger.fingerprint")
    
    def compute_fingerprint(self, node: ASTNode, normalize: bool = True) -> ASTFingerprint:
        """
        Compute multi-level fingerprint of AST subtree.
        
        Args:
            node: AST node to fingerprint
            normalize: If True, ignore variable names for structural similarity
        
        Returns:
            ASTFingerprint object with structural features
        """
        if node is None:
            return ASTFingerprint()
        
        # Extract node sequence (pre-order traversal)
        node_seq = self._extract_node_sequence(node, normalize)
        
        # Extract subtree patterns (depth-limited for efficiency)
        subtree_patterns = self._extract_subtree_patterns(node, max_depth=3, normalize=normalize)
        
        # Compute statistical features
        depth = self._compute_depth(node)
        size = len(node_seq)
        feature_vec = self._build_feature_vector(node_seq)
        
        return ASTFingerprint(
            node_sequence=node_seq,
            subtree_patterns=subtree_patterns,
            depth=depth,
            size=size,
            feature_vector=feature_vec,
            ast_node=node
        )
    
    def _extract_node_sequence(self, node: ASTNode, normalize: bool = True) -> List[str]:
        """Extract ordered sequence of node types (pre-order traversal)."""
        sequence = []
        
        def traverse(n):
            # Add normalized representation of node
            if normalize:
                if _is_identifier_like(n):
                    node_repr = f"{n.kind}:ID"
                elif _is_literal(n):
                    node_repr = f"{n.kind}:LIT"
                elif n.token and _should_keep_token(n, n.token):
                    node_repr = f"{n.kind}:{n.token}"
                else:
                    node_repr = n.kind
            else:
                node_repr = f"{n.kind}:{n.token}" if n.token else n.kind
            
            sequence.append(node_repr)
            
            for child in n.children:
                traverse(child)
        
        traverse(node)
        return sequence
    
    def _extract_subtree_patterns(self, node: ASTNode, max_depth: int = 3, normalize: bool = True) -> Set[str]:
        """
        Extract subtree patterns up to certain depth.
        Uses string representation instead of hashing for pattern matching.
        """
        patterns = set()
        
        def traverse(n, depth, path):
            if depth > max_depth:
                return
            
            # Create node representation
            if normalize:
                if _is_identifier_like(n):
                    node_repr = f"{n.kind}:ID"
                elif _is_literal(n):
                    node_repr = f"{n.kind}:LIT"
                elif n.token and _should_keep_token(n, n.token):
                    node_repr = f"{n.kind}:{n.token}"
                else:
                    node_repr = n.kind
            else:
                node_repr = f"{n.kind}:{n.token}" if n.token else n.kind
            
            current_pattern = "->".join(path + [node_repr])
            patterns.add(current_pattern)
            
            for child in n.children:
                traverse(child, depth + 1, path + [node_repr])
        
        traverse(node, 0, [])
        return patterns
    
    def _build_feature_vector(self, node_types: List[str]) -> Dict[str, int]:
        """Build frequency vector of node types."""
        return dict(Counter(node_types))
    
    def _compute_depth(self, node: ASTNode) -> int:
        """Compute tree depth."""
        if not node.children:
            return 1
        return 1 + max(self._compute_depth(child) for child in node.children)
    
    def _is_identifier_like(self, node: ASTNode) -> bool:
        """Check if node is an identifier or declaration."""
        identifier_kinds = {
            "DECL_REF_EXPR", "VAR_DECL", "PARM_DECL", "FUNCTION_DECL",
            "identifier", "field_identifier", "type_identifier",
            "UNEXPOSED_EXPR"  # Often contains variable references
        }
        return node.kind in identifier_kinds
    
    def _is_literal(self, node: ASTNode) -> bool:
        """Check if node is a literal value."""
        literal_kinds = {
            "INTEGER_LITERAL", "FLOATING_LITERAL", "STRING_LITERAL",
            "CHARACTER_LITERAL", "number_literal", "string_literal",
            "char_literal"
        }
        return node.kind in literal_kinds
    
    def _should_keep_token(self, node: ASTNode, token: str) -> bool:
        """
        Determine if a token should be preserved in fingerprint.
        Only keep operators and built-in function names.
        """
        if not token:
            return False
        
        # Keep operators
        operators = {
            '+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=',
            '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', 
            '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=',
            '++', '--', '->', '.', '?', ':'
        }
        if token in operators:
            return True
        
        # Keep keywords
        keywords = {
            'if', 'else', 'while', 'for', 'do', 'switch', 'case', 'default',
            'break', 'continue', 'return', 'goto', 'sizeof', 'typeof'
        }
        if token in keywords:
            return True
        
        # Keep standard library function names (common ones)
        stdlib_funcs = {
            'printf', 'scanf', 'malloc', 'free', 'memcpy', 'memset',
            'strlen', 'strcmp', 'strcpy', 'fopen', 'fclose', 'fread', 'fwrite',
            'abs', 'sqrt', 'pow', 'sin', 'cos', 'modf', 'floor', 'ceil'
        }
        if token in stdlib_funcs:
            return True
        
        # Don't keep user-defined names
        return False
    
    def extract_fragments(self, ast: ASTNode, prog_id: str, clause_id: str) -> List[Fragment]:
        """Extract meaningful code fragments from AST."""
        fragments = []
        fragment_counter = [0]  # Use list for mutable counter
        
        def extract_recursive(node: ASTNode, position: int) -> None:
            # Extract fragments for meaningful node types
            if self._is_fragment_worthy(node):
                fp = self.compute_fingerprint(node)
                frag_id = f"{prog_id}_{clause_id}_f{fragment_counter[0]}"
                fragment_counter[0] += 1
                
                fragments.append(Fragment(
                    prog_id=prog_id,
                    clause_id=clause_id,
                    fragment_id=frag_id,
                    ast=node,
                    code_snippet=self._node_to_code(node),
                    fingerprint=fp,
                    position=position
                ))
            
            # Recurse on children
            for i, child in enumerate(node.children):
                extract_recursive(child, position + i)
        
        extract_recursive(ast, 0)
        return fragments
    
    def _is_fragment_worthy(self, node: ASTNode) -> bool:
        """Determine if node is worth extracting as a fragment."""
        worthy_kinds = {
            # Statements
            "IF_STMT", "WHILE_STMT", "FOR_STMT", "DO_STMT",
            "RETURN_STMT", "COMPOUND_STMT",
            # Expressions
            "CALL_EXPR", "BINARY_OPERATOR", "UNARY_OPERATOR",
            # Declarations
            "VAR_DECL", "FUNCTION_DECL",
            # Tree-sitter equivalents
            "if_statement", "while_statement", "for_statement",
            "return_statement", "compound_statement",
            "call_expression", "binary_expression",
            "declaration"
        }
        
        return node.kind in worthy_kinds
    
    def _node_to_code(self, node: ASTNode) -> str:
        """Convert AST node to approximate code snippet."""
        # For now, reconstruct code by traversing the tree
        # This is a simplified version - ideally use original source ranges
        
        if node.kind == "INTEGER_LITERAL":
            return node.token
        elif node.kind == "STRING_LITERAL":
            return f'"{node.token}"'
        elif node.kind == "BINARY_OPERATOR":
            if len(node.children) >= 2:
                left = self._node_to_code(node.children[0])
                right = self._node_to_code(node.children[1])
                op = node.token if node.token else "+"
                return f"{left} {op} {right}"
        elif node.kind == "CALL_EXPR":
            if node.children:
                func = self._node_to_code(node.children[0])
                args = [self._node_to_code(c) for c in node.children[1:]]
                return f"{func}({', '.join(args)})"
        elif node.kind == "RETURN_STMT":
            if node.children:
                expr = self._node_to_code(node.children[0])
                return f"return {expr};"
            return "return;"
        elif node.kind == "VAR_DECL":
            type_name = "int"  # Simplified
            var_name = node.token if node.token else "var"
            if node.children:
                init = self._node_to_code(node.children[0])
                return f"{type_name} {var_name} = {init};"
            return f"{type_name} {var_name};"
        elif node.kind in ["DECL_REF_EXPR", "identifier"]:
            return node.token if node.token else ""
        
        # Default: join children
        if not node.children:
            return node.token if node.token else ""
        
        parts = [self._node_to_code(child) for child in node.children]
        parts = [p for p in parts if p]  # Filter empty strings
        
        # Add semicolons for statements
        if node.kind in ["IF_STMT", "WHILE_STMT", "FOR_STMT"]:
            return " ".join(parts)
        
        return " ".join(parts)
    
    def compute_similarity(self, fp1: str, fp2: str) -> float:
        """Compute similarity between two fingerprints (0.0 to 1.0)."""
        # Exact match
        if fp1 == fp2:
            return 1.0
        
        # For different fingerprints, use a simple metric
        # In practice, you might use edit distance on the ASTs
        return 0.0
    
    def find_consensus_fragments(
        self,
        all_fragments: List[List[Fragment]],
        threshold: float = 0.6
    ) -> List[Fragment]:
        """
        Find consensus fragments across multiple programs using structural similarity.
        
        Args:
            all_fragments: List of fragment lists, one per program
            threshold: Minimum fraction of programs that must agree
        
        Returns:
            List of consensus fragments
        """
        if not all_fragments:
            return []
        
        # Flatten all fragments
        all_frags_flat = []
        for frag_list in all_fragments:
            all_frags_flat.extend(frag_list)
        
        if not all_frags_flat:
            return []
        
        # Group similar fragments using similarity-based clustering
        num_programs = len(all_fragments)
        min_count = int(threshold * num_programs)
        
        # Cluster fragments by similarity
        clusters = self._cluster_fragments_by_similarity(all_frags_flat, similarity_threshold=0.75)
        
        # Filter clusters that meet the threshold
        consensus = []
        for cluster in clusters:
            # Count how many different programs are represented
            prog_ids = set(frag.prog_id for frag in cluster)
            if len(prog_ids) >= min_count:
                # Pick representative fragment (one with best average similarity to others)
                representative = self._find_cluster_representative(cluster)
                consensus.append(representative)
        
        # Sort by average position
        consensus.sort(key=lambda f: f.position)
        
        self.logger.info(f"Found {len(consensus)} consensus fragments from {len(clusters)} clusters")
        
        return consensus
    
    def _cluster_fragments_by_similarity(
        self,
        fragments: List[Fragment],
        similarity_threshold: float = 0.75
    ) -> List[List[Fragment]]:
        """
        Cluster fragments based on structural similarity (not hashing).
        Uses single-linkage clustering with similarity threshold.
        """
        n = len(fragments)
        if n == 0:
            return []
        if n == 1:
            return [[fragments[0]]]
        
        # Compute similarity matrix
        similarities = np.zeros((n, n))
        for i in range(n):
            similarities[i][i] = 1.0
            for j in range(i + 1, n):
                sim = fragments[i].fingerprint.similarity(fragments[j].fingerprint)
                similarities[i][j] = sim
                similarities[j][i] = sim
        
        # Greedy clustering: start with each fragment, grow cluster
        visited = [False] * n
        clusters = []
        
        for i in range(n):
            if visited[i]:
                continue
            
            # Start new cluster
            cluster = [fragments[i]]
            visited[i] = True
            
            # Find all fragments within similarity threshold
            for j in range(n):
                if not visited[j] and similarities[i][j] >= similarity_threshold:
                    cluster.append(fragments[j])
                    visited[j] = True
            
            clusters.append(cluster)
        
        self.logger.debug(f"Clustered {n} fragments into {len(clusters)} clusters using similarity")
        
        return clusters
    
    def _find_cluster_representative(self, cluster: List[Fragment]) -> Fragment:
        """Find the fragment with best average similarity to others in cluster."""
        if len(cluster) == 1:
            return cluster[0]
        
        best_frag = cluster[0]
        best_avg_sim = 0.0
        
        for frag in cluster:
            # Compute average similarity to all others
            similarities = [frag.fingerprint.similarity(other.fingerprint) 
                          for other in cluster if other != frag]
            avg_sim = sum(similarities) / len(similarities) if similarities else 0.0
            
            if avg_sim > best_avg_sim:
                best_avg_sim = avg_sim
                best_frag = frag
        
        return best_frag
    
    def compute_jaccard_similarity(self, fp1: ASTFingerprint, fp2: ASTFingerprint) -> float:
        """Compute Jaccard similarity between two ASTFingerprints."""
        return fp1._jaccard_similarity(fp2)
    
    def cluster_fingerprints(
        self,
        fingerprints: List[ASTFingerprint],
        similarity_threshold: float = 0.75
    ) -> List[List[int]]:
        """
        Cluster fingerprints based on structural similarity (not hash edit distance).
        
        Args:
            fingerprints: List of ASTFingerprint objects
            similarity_threshold: Minimum similarity for grouping (default: 0.75)
        
        Returns:
            List of clusters, where each cluster is a list of indices
        """
        n = len(fingerprints)
        if n == 0:
            return []
        if n == 1:
            return [[0]]
        
        # Compute pairwise similarity matrix
        similarities = np.zeros((n, n))
        for i in range(n):
            similarities[i][i] = 1.0
            for j in range(i + 1, n):
                sim = fingerprints[i].similarity(fingerprints[j])
                similarities[i][j] = sim
                similarities[j][i] = sim
        
        # Greedy clustering: start with each point, grow cluster
        visited = [False] * n
        clusters = []
        
        for i in range(n):
            if visited[i]:
                continue
            
            # Start new cluster
            cluster = [i]
            visited[i] = True
            
            # Find all points within similarity threshold
            for j in range(n):
                if not visited[j] and similarities[i][j] >= similarity_threshold:
                    cluster.append(j)
                    visited[j] = True
            
            clusters.append(cluster)
        
        self.logger.debug(f"Clustered {n} fingerprints into {len(clusters)} clusters using similarity threshold {similarity_threshold}")
        
        return clusters
    
    def compute_cluster_confidence(
        self,
        cluster_indices: List[int],
        fingerprints: List[ASTFingerprint],
        total_count: int
    ) -> float:
        """
        Compute confidence score for a cluster based on similarity variance.
        
        Args:
            cluster_indices: Indices of fingerprints in the cluster
            fingerprints: Full list of fingerprints
            total_count: Total number of implementations
        
        Returns:
            Confidence score (0.0 to 1.0)
        """
        logger = logging.getLogger("ast_merger.fingerprint")
        logger.info(f"Computing confidence: cluster_size={len(cluster_indices)}, total={total_count}")
        
        if len(cluster_indices) == 0:
            return 0.0
        
        # Base confidence from cluster size
        base_confidence = len(cluster_indices) / total_count
        logger.info(f"Base confidence: {base_confidence:.3f}")
        
        if len(cluster_indices) == 1:
            return base_confidence
        
        # Compute all pairwise similarities within cluster
        similarities = []
        for i in range(len(cluster_indices)):
            for j in range(i + 1, len(cluster_indices)):
                idx_i = cluster_indices[i]
                idx_j = cluster_indices[j]
                sim = fingerprints[idx_i].similarity(fingerprints[idx_j])
                similarities.append(sim)
                logger.info(f"  Similarity between {idx_i} and {idx_j}: {sim:.3f}")
        
        # Average similarity within cluster (higher is better)
        if similarities:
            avg_similarity = sum(similarities) / len(similarities)
            logger.info(f"Average internal similarity: {avg_similarity:.3f}")
            # Confidence is base confidence boosted by internal similarity
            confidence = base_confidence * avg_similarity
            logger.info(f"Final confidence: {confidence:.3f}")
        else:
            confidence = base_confidence
        
        return confidence
