#!/usr/bin/env python3
"""
AST fingerprinting using tree edit distance and structural similarity.
Implements Zhang-Shasha tree edit distance algorithm for accurate AST comparison.
Language agnostic version.
"""

import hashlib
import logging
import numpy as np
import signal
import threading
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict, Counter
from dataclasses import dataclass, field
from tools.parser_base import ASTNode
from tools.language_configs import get_language_config

class TreeTooLargeForTED(Exception):
    """Raised when a tree exceeds ted_max_nodes; caller falls back to the fast blend."""

    def __init__(self, size: int):
        super().__init__(f"tree of {size} nodes exceeds the TED limit")
        self.size = size


class TreeEditDistanceTimedOut(Exception):
    """Raised when TED exceeds ted_timeout_seconds; caller falls back to the fast blend."""


# Global cache for tree edit distance computations
_ted_cache: Dict[Tuple[str, str], int] = {}


@dataclass
class ASTFingerprint:
    """
    Multi-level fingerprint for similarity-preserving AST comparison.
    Does not rely on hashing for similarity - uses structural features.
    """
    node_sequence: List[str] = field(default_factory=list)
    subtree_patterns: Set[str] = field(default_factory=set)
    depth: int = 0
    size: int = 0
    feature_vector: Dict[str, int] = field(default_factory=dict)
    ast_node: Optional[ASTNode] = None
    # Ordering-sensitive and weighted structural features (see SIMILARITY_DEFAULTS).
    ngram_counts: Counter = field(default_factory=Counter)
    pattern_counts: Counter = field(default_factory=Counter)
    structural_key: str = ""

    # Store the fingerprint config internally to compute Jaccard properly
    
    def similarity(self, other: 'ASTFingerprint') -> float:
        """Structural similarity in [0, 1].

        The fast blend is always computed: it is the value used directly for
        languages without tree edit distance, and it is also the fallback for
        every case where TED cannot produce a trustworthy answer (missing AST,
        trees too large to align, trees too different in size to align). Those
        fallbacks used to return arbitrary scalings (``size_ratio * 0.5``,
        ``0.3 * jaccard``) or, for oversized trees, a distance equal to the tree
        size -- which drove the similarity term to exactly 0 and split clauses
        that were in fact near-identical. They now degrade to the fast blend,
        which is continuous with the TED path and calibrated on the same scale.
        """
        if self.size == 0 and other.size == 0:
            return 1.0
        if self.size == 0 or other.size == 0:
            return 0.0

        fast = self._fast_similarity(other)

        if not self.config.get("use_tree_edit_distance", True):
            return fast
        if self.ast_node is None or other.ast_node is None:
            return fast

        max_size = max(self.size, other.size)
        size_ratio = min(self.size, other.size) / max_size
        if size_ratio < self.config.get("ted_min_size_ratio", 0.34):
            return fast
        if max_size > self.config.get("ted_max_nodes", 500):
            return fast

        try:
            tree_distance = tree_edit_distance_with_timeout(self.ast_node, other.ast_node, self.config)
        except (TreeTooLargeForTED, TreeEditDistanceTimedOut):
            return fast
        tree_sim = max(0.0, 1.0 - (tree_distance / max_size))
        w = self.config.get("ted_weight", 0.60)
        return w * tree_sim + (1.0 - w) * fast

    def _fast_similarity(self, other: 'ASTFingerprint') -> float:
        """Weighted blend of ordering, node-kind and ancestry-path agreement.

        Every term is a weighted (multiset) Jaccard, so an unrelated pair scores
        near 0 on each rather than inheriting a floor from ratio terms.
        """
        weights = self.config.get("similarity_weights", {})
        ngram = _weighted_jaccard(self.ngram_counts, other.ngram_counts)
        kinds = self._feature_similarity(other)
        paths = _weighted_jaccard(self.pattern_counts, other.pattern_counts)
        size_ratio = (min(self.size, other.size) / max(self.size, other.size)
                      if max(self.size, other.size) > 0 else 1.0)
        score = (weights.get("ngram", 0.30) * ngram
                 + weights.get("kinds", 0.45) * kinds
                 + weights.get("paths", 0.20) * paths
                 + weights.get("size", 0.05) * size_ratio)
        total = sum(weights.get(k, d) for k, d in
                    (("ngram", 0.30), ("kinds", 0.45), ("paths", 0.20), ("size", 0.05)))
        return score / total if total > 0 else 0.0

    def _fallback_similarity(self, other: 'ASTFingerprint') -> float:
        """Kept for callers that ask for the no-AST path explicitly."""
        return self._fast_similarity(other)
    
    def _jaccard_similarity(self, other: 'ASTFingerprint') -> float:
        if not self.subtree_patterns and not other.subtree_patterns:
            return 1.0
        
        intersection = len(self.subtree_patterns & other.subtree_patterns)
        union = len(self.subtree_patterns | other.subtree_patterns)
        
        return intersection / union if union > 0 else 0.0

    def _feature_similarity(self, other: 'ASTFingerprint') -> float:
        if not self.feature_vector and not other.feature_vector:
            return 1.0

        keys = set(self.feature_vector) | set(other.feature_vector)
        overlap = sum(min(self.feature_vector.get(k, 0), other.feature_vector.get(k, 0)) for k in keys)
        total = sum(max(self.feature_vector.get(k, 0), other.feature_vector.get(k, 0)) for k in keys)
        return overlap / total if total > 0 else 0.0


def _weighted_jaccard(a: Counter, b: Counter) -> float:
    """Multiset Jaccard: sum(min) / sum(max). 1.0 when both sides are empty."""
    if not a and not b:
        return 1.0
    keys = set(a) | set(b)
    union = sum(max(a.get(k, 0), b.get(k, 0)) for k in keys)
    if union == 0:
        return 0.0
    return sum(min(a.get(k, 0), b.get(k, 0)) for k in keys) / union


@dataclass
class Fragment:
    """Code fragment with metadata."""
    prog_id: str
    clause_id: str
    fragment_id: str
    ast: ASTNode
    code_snippet: str
    fingerprint: ASTFingerprint
    position: int


def structural_digest(node: ASTNode, config: Dict) -> str:
    """Content hash of a normalized subtree.

    The TED cache used to be keyed on ``id(node)``. CPython recycles ids once an
    object is freed, so a cache entry could be returned for a completely
    different tree that happened to reuse the address -- silently wrong
    distances, and only invisible today because the engine keeps every parsed
    AST alive for the duration of a run. Keying on structure is both correct and
    a better cache: identical subtrees from different programs now share it.
    """
    parts: List[str] = []

    def walk(n: ASTNode) -> None:
        parts.append(_normalize_token(n, config))
        parts.append(n.kind)
        parts.append("(")
        for child in n.children:
            walk(child)
        parts.append(")")

    walk(node)
    return hashlib.sha1("\x00".join(parts).encode("utf-8")).hexdigest()


def tree_edit_distance_cached(tree1: ASTNode, tree2: ASTNode, config: Dict) -> int:
    """Cached wrapper for TED computation, keyed on tree structure."""
    if tree1 is None and tree2 is None:
        return 0
    if tree1 is None:
        return _count_nodes(tree2)
    if tree2 is None:
        return _count_nodes(tree1)

    key1 = structural_digest(tree1, config)
    key2 = structural_digest(tree2, config)
    if key1 == key2:
        return 0
    cache_key = (min(key1, key2), max(key1, key2))

    if cache_key in _ted_cache:
        return _ted_cache[cache_key]

    distance = tree_edit_distance(tree1, tree2, config)
    _ted_cache[cache_key] = distance
    return distance


def tree_edit_distance_with_timeout(tree1: ASTNode, tree2: ASTNode, config: Dict) -> int:
    """Run cached TED with a per-comparison wall-clock timeout when possible."""
    timeout = config.get("ted_timeout_seconds", 0)
    if not timeout:
        return tree_edit_distance_cached(tree1, tree2, config)
    if threading.current_thread() is not threading.main_thread() or not hasattr(signal, "SIGALRM"):
        return tree_edit_distance_cached(tree1, tree2, config)

    def on_timeout(signum, frame):
        raise TreeEditDistanceTimedOut(f"TED exceeded {timeout}s")

    old_handler = signal.getsignal(signal.SIGALRM)
    old_timer = signal.getitimer(signal.ITIMER_REAL)
    signal.signal(signal.SIGALRM, on_timeout)
    signal.setitimer(signal.ITIMER_REAL, float(timeout))
    try:
        return tree_edit_distance_cached(tree1, tree2, config)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old_handler)
        if old_timer[0] > 0:
            signal.setitimer(signal.ITIMER_REAL, old_timer[0], old_timer[1])


def tree_edit_distance(tree1: ASTNode, tree2: ASTNode, config: Dict) -> int:
    """
    Compute tree edit distance using Zhang-Shasha algorithm.
    """
    if tree1 is None and tree2 is None: return 0
    if tree1 is None: return _count_nodes(tree2)
    if tree2 is None: return _count_nodes(tree1)
    
    if _nodes_equal(tree1, tree2, config) and not tree1.children and not tree2.children:
        return 0
    
    size1 = _count_nodes(tree1)
    size2 = _count_nodes(tree2)
    limit = config.get("ted_max_nodes", 500)
    if size1 > limit or size2 > limit:
        # Callers are expected to fall back to the fast blend before getting
        # here. Returning max(size) would report "maximally different", which is
        # what previously collapsed every large clause to similarity ~0.3.
        raise TreeTooLargeForTED(max(size1, size2))
    
    keyroots1, lmld1 = _compute_keyroots_and_lmld(tree1)
    keyroots2, lmld2 = _compute_keyroots_and_lmld(tree2)
    
    nodes1 = _postorder_nodes(tree1)
    nodes2 = _postorder_nodes(tree2)
    
    n1, n2 = len(nodes1), len(nodes2)
    tree_dist = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    
    for i in keyroots1:
        for j in keyroots2:
            forest_dist = [[0] * (n2 + 1) for _ in range(n1 + 1)]
            
            for di in range(lmld1[i], i + 1):
                forest_dist[di][0] = forest_dist[di - 1][0] + 1
            for dj in range(lmld2[j], j + 1):
                forest_dist[0][dj] = forest_dist[0][dj - 1] + 1
            
            for di in range(lmld1[i], i + 1):
                for dj in range(lmld2[j], j + 1):
                    node1 = nodes1[di - 1]
                    node2 = nodes2[dj - 1]
                    
                    cost = 0 if _nodes_equal(node1, node2, config) else 1
                    
                    if lmld1[di] == lmld1[i] and lmld2[dj] == lmld2[j]:
                        forest_dist[di][dj] = min(
                            forest_dist[di - 1][dj] + 1,
                            forest_dist[di][dj - 1] + 1,
                            forest_dist[di - 1][dj - 1] + cost
                        )
                        tree_dist[di][dj] = forest_dist[di][dj]
                    else:
                        forest_dist[di][dj] = min(
                            forest_dist[di - 1][dj] + 1,
                            forest_dist[di][dj - 1] + 1,
                            forest_dist[lmld1[di] - 1][lmld2[dj] - 1] + tree_dist[di][dj]
                        )
    
    return tree_dist[n1][n2]


def _count_nodes(node: ASTNode) -> int:
    if node is None: return 0
    count = 1
    for child in node.children:
        count += _count_nodes(child)
    return count

def _postorder_nodes(node: ASTNode) -> List[ASTNode]:
    nodes = []
    def traverse(n):
        for child in n.children:
            traverse(child)
        nodes.append(n)
    traverse(node)
    return nodes

def _compute_keyroots_and_lmld(root: ASTNode) -> Tuple[List[int], Dict[int, int]]:
    nodes = _postorder_nodes(root)
    n = len(nodes)
    
    lmld = {}
    for i, node in enumerate(nodes, start=1):
        if not node.children:
            lmld[i] = i
        else:
            leftmost_child = node.children[0]
            leftmost_idx = nodes.index(leftmost_child) + 1
            lmld[i] = lmld[leftmost_idx]
    
    keyroots_set = set()
    for i in range(1, n + 1):
        l = lmld[i]
        if l not in keyroots_set:
            keyroots_set.add(l)
    
    keyroots_set.add(n)
    return sorted(keyroots_set), lmld

def _nodes_equal(node1: ASTNode, node2: ASTNode, config: Dict) -> bool:
    if node1.kind != node2.kind:
        return False
    
    token1 = _normalize_token(node1, config)
    token2 = _normalize_token(node2, config)
    return token1 == token2

def _normalize_token(node: ASTNode, config: Dict) -> str:
    if node.kind in config["identifier_kinds"]:
        return "ID"
    elif node.kind in config["literal_kinds"]:
        return "LIT"
    elif node.token and _should_keep_token(node.token, config):
        return node.token
    else:
        return ""

def _should_keep_token(token: str, config: Dict) -> bool:
    if not token:
        return False
    
    if token in config["operators"]: return True
    if token in config["keywords"]: return True
    if token in config["stdlib_funcs"]: return True
    
    return False


class Fingerprinter:
    """Computes multi-level fingerprints for AST subtrees using language configs."""
    
    def __init__(self, lang: str):
        self.logger = logging.getLogger("ast_merger.fingerprint")
        self.config = get_language_config(lang)
    
    def compute_fingerprint(self, node: ASTNode, normalize: bool = True) -> ASTFingerprint:
        if node is None:
            fp = ASTFingerprint()
            fp.config = self.config
            return fp
            
        node_seq = self._extract_node_sequence(node, normalize)
        subtree_patterns = self._extract_subtree_patterns(node, max_depth=3, normalize=normalize)

        pattern_depth = self.config.get("similarity_pattern_depth", 4)
        pattern_counts = self._extract_pattern_counts(node, pattern_depth, normalize)
        k = self.config.get("similarity_ngram", 3)
        ngram_counts = Counter(
            tuple(node_seq[i:i + k]) for i in range(max(0, len(node_seq) - k + 1))
        )

        depth = self._compute_depth(node)
        size = len(node_seq)
        feature_vec = dict(Counter(node_seq))

        fp = ASTFingerprint(
            node_sequence=node_seq,
            subtree_patterns=subtree_patterns,
            depth=depth,
            size=size,
            feature_vector=feature_vec,
            ast_node=node,
            ngram_counts=ngram_counts,
            pattern_counts=pattern_counts,
            structural_key=hashlib.sha1("\x00".join(node_seq).encode("utf-8")).hexdigest(),
        )
        fp.config = self.config
        return fp

    def _extract_pattern_counts(self, node: ASTNode, max_depth: int, normalize: bool) -> Counter:
        """Weighted ancestry paths: like subtree_patterns but deeper and counted.

        The depth-3 *set* of paths saturates -- unrelated Python clauses share
        almost every short path, which is why 30% of unrelated pairs used to
        score above the old 0.70 threshold. Going deeper and keeping
        multiplicities restores discrimination.
        """
        counts: Counter = Counter()

        def traverse(n: ASTNode, depth: int, path: List[str]) -> None:
            if depth > max_depth:
                return
            node_repr = self._node_repr(n, normalize)
            current = "->".join(path + [node_repr])
            counts[current] += 1
            for child in n.children:
                traverse(child, depth + 1, path + [node_repr])

        traverse(node, 0, [])
        return counts

    def _node_repr(self, n: ASTNode, normalize: bool) -> str:
        if not normalize:
            return f"{n.kind}:{n.token}" if n.token else n.kind
        if n.kind in self.config["identifier_kinds"]:
            return f"{n.kind}:ID"
        if n.kind in self.config["literal_kinds"]:
            return f"{n.kind}:LIT"
        if n.token and _should_keep_token(n.token, self.config):
            return f"{n.kind}:{n.token}"
        return n.kind
    
    def _extract_node_sequence(self, node: ASTNode, normalize: bool = True) -> List[str]:
        sequence = []
        def traverse(n):
            if normalize:
                if n.kind in self.config["identifier_kinds"]:
                    node_repr = f"{n.kind}:ID"
                elif n.kind in self.config["literal_kinds"]:
                    node_repr = f"{n.kind}:LIT"
                elif n.token and _should_keep_token(n.token, self.config):
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
        patterns = set()
        def traverse(n, depth, path):
            if depth > max_depth: return
            
            if normalize:
                if n.kind in self.config["identifier_kinds"]:
                    node_repr = f"{n.kind}:ID"
                elif n.kind in self.config["literal_kinds"]:
                    node_repr = f"{n.kind}:LIT"
                elif n.token and _should_keep_token(n.token, self.config):
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
    
    def _compute_depth(self, node: ASTNode) -> int:
        if not node.children: return 1
        return 1 + max(self._compute_depth(child) for child in node.children)
    
    def extract_fragments(self, ast: ASTNode, prog_id: str, clause_id: str) -> List[Fragment]:
        fragments = []
        fragment_counter = [0]
        
        def extract_recursive(node: ASTNode, position: int) -> None:
            if node.kind in self.config.get("worthy_kinds", set()):
                fp = self.compute_fingerprint(node)
                frag_id = f"{prog_id}_{clause_id}_f{fragment_counter[0]}"
                fragment_counter[0] += 1
                
                fragments.append(Fragment(
                    prog_id=prog_id,
                    clause_id=clause_id,
                    fragment_id=frag_id,
                    ast=node,
                    code_snippet=node.token, # Simplified snippet
                    fingerprint=fp,
                    position=position
                ))
            
            for i, child in enumerate(node.children):
                extract_recursive(child, position + i)
        
        extract_recursive(ast, 0)
        return fragments

    def similarity_matrix(self, fingerprints: List[ASTFingerprint]) -> np.ndarray:
        n = len(fingerprints)
        sims = np.eye(n)
        for i in range(n):
            for j in range(i + 1, n):
                s = fingerprints[i].similarity(fingerprints[j])
                sims[i][j] = s
                sims[j][i] = s
        return sims

    def cluster_fingerprints(
        self,
        fingerprints: List[ASTFingerprint],
        similarity_threshold: float = 0.60
    ) -> List[List[int]]:
        """Complete-linkage threshold clustering.

        The previous version seeded a cluster with the first unvisited index and
        absorbed every unvisited j with sim(seed, j) >= threshold. Members were
        never compared to each other, so a chain of pairwise-similar variants
        could land in one cluster while being mutually dissimilar, and the result
        depended on the order programs happened to appear in the input file.

        Here a variant joins a cluster only if it is within threshold of *every*
        current member, and seeds are taken in order of decreasing total
        similarity, so the most representative variant anchors the first cluster
        and the result no longer depends on input order.
        """
        n = len(fingerprints)
        if n == 0:
            return []
        if n == 1:
            return [[0]]

        similarities = self.similarity_matrix(fingerprints)

        # Most central variants first: deterministic and order-independent.
        order = sorted(range(n), key=lambda i: (float(similarities[i].sum()), -i), reverse=True)

        assigned = [False] * n
        clusters: List[List[int]] = []

        for seed in order:
            if assigned[seed]:
                continue
            cluster = [seed]
            assigned[seed] = True
            for j in order:
                if assigned[j]:
                    continue
                if all(similarities[j][m] >= similarity_threshold for m in cluster):
                    cluster.append(j)
                    assigned[j] = True
            clusters.append(sorted(cluster))

        return clusters
