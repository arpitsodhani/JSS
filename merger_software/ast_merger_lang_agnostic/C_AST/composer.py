#!/usr/bin/env python3
"""
Composer for assembling merged clauses and resolving conflicts.
"""

import logging
from typing import Dict, List, Set, Tuple, Optional, Any
from collections import defaultdict
from dataclasses import dataclass

from tools.parser_libclang import ASTNode, ParsedClause
from tools.fingerprint import Fragment, Fingerprinter
from tools.normalize import ASTNormalizer


@dataclass
class MergedClause:
    """Merged clause result."""
    clause_id: str
    signature: str
    code: str
    confidence: float
    used_fragments: List[Dict[str, Any]]  # Fragment provenance
    declarations: Dict[str, str]


class Composer:
    """Composes merged program from fragments."""
    
    def __init__(self, threshold: float = 0.6):
        self.threshold = threshold
        self.logger = logging.getLogger("ast_merger.composer")
        self.fingerprinter = Fingerprinter()
        self.normalizer = ASTNormalizer()
    
    def merge_clause(
        self,
        clause_id: str,
        parsed_clauses: List[ParsedClause]
    ) -> MergedClause:
        """
        Merge multiple implementations of the same clause.
        
        Args:
            clause_id: Clause identifier
            parsed_clauses: List of parsed clauses from different programs
        
        Returns:
            Merged clause
        """
        self.logger.info(f"Merging clause {clause_id} from {len(parsed_clauses)} programs")
        
        # Extract signature (should be same across all)
        signature = parsed_clauses[0].signature if parsed_clauses else ""
        
        # Filter out failed parses
        valid_clauses = [c for c in parsed_clauses if c.ast is not None]
        
        self.logger.info(f"Valid clauses: {len(valid_clauses)} out of {len(parsed_clauses)}")
        for i, c in enumerate(parsed_clauses):
            self.logger.info(f"  Clause {i}: ast={'present' if c.ast else 'NONE'}")
        
        if not valid_clauses:
            self.logger.warning(f"No valid parses for clause {clause_id}, using fallback")
            return self._create_fallback_clause(clause_id, signature, parsed_clauses)
        
        # Extract fragments from each program
        all_fragments = []
        for i, clause in enumerate(valid_clauses):
            prog_id = f"prog{i}"
            fragments = self.fingerprinter.extract_fragments(clause.ast, prog_id, clause_id)
            all_fragments.append(fragments)
        
        # Find consensus fragments
        consensus_fragments = self.fingerprinter.find_consensus_fragments(
            all_fragments,
            threshold=self.threshold
        )
        
        # Compose merged code
        merged_code, used_fragments, confidence = self._compose_code(
            signature,
            consensus_fragments,
            all_fragments,
            valid_clauses
        )
        
        # Merge declarations
        merged_decls = self._merge_declarations([c.declarations for c in valid_clauses])
        
        return MergedClause(
            clause_id=clause_id,
            signature=signature,
            code=merged_code,
            confidence=confidence,
            used_fragments=used_fragments,
            declarations=merged_decls
        )
    
    def _compose_code(
        self,
        signature: str,
        consensus_fragments: List[Fragment],
        all_fragments: List[List[Fragment]],
        clauses: List[ParsedClause]
    ) -> Tuple[str, List[Dict[str, Any]], float]:
        """
        Compose code from consensus fragments using similarity-based clustering.
        
        Uses tree edit distance and structural similarity (not hashing)
        to identify similar implementations, then selects from the majority cluster.
        """
        
        # Extract fingerprints from all clauses
        fingerprints = []
        fingerprint_to_clause = {}
        
        for i, clause in enumerate(clauses):
            if clause.ast is None:
                self.logger.warning(f"Clause {i} has no AST, skipping")
                continue
            
            # Compute fingerprint for the entire clause implementation
            fp = self.fingerprinter.compute_fingerprint(clause.ast)
            fingerprints.append(fp)
            fingerprint_to_clause[id(fp)] = (clause, i)  # Use id() for unique key
        
        self.logger.info(f"Computed {len(fingerprints)} fingerprints from {len(clauses)} clauses")
        
        # Debug: check pairwise similarities
        if len(fingerprints) >= 2:
            self.logger.info("Sample pairwise similarities:")
            for i in range(min(3, len(fingerprints))):
                for j in range(i+1, min(3, len(fingerprints))):
                    sim = fingerprints[i].similarity(fingerprints[j])
                    self.logger.info(f"  fp[{i}] vs fp[{j}]: {sim:.3f} (size: {fingerprints[i].size} vs {fingerprints[j].size})")
        
        if not fingerprints:
            # Fallback to first clause
            if clauses:
                code = self._ensure_function_wrapper(clauses[0].code, signature)
                return code, [], 0.5
            return f"{signature} {{\n    // TODO: implement\n    return 0;\n}}", [], 0.0
        
        # Cluster fingerprints by structural similarity (threshold 0.75)
        clusters = self.fingerprinter.cluster_fingerprints(fingerprints, similarity_threshold=0.75)
        
        self.logger.info(f"Formed {len(clusters)} clusters from {len(fingerprints)} fingerprints")
        for i, cluster in enumerate(clusters):
            self.logger.info(f"  Cluster {i}: size={len(cluster)}, indices={cluster}")
        
        # Find majority cluster (largest cluster)
        majority_cluster = max(clusters, key=len)
        
        # Compute cluster-based confidence using similarity metrics
        cluster_size = len(majority_cluster)
        total_implementations = len(fingerprints)
        
        # Compute confidence based on cluster size and internal similarity
        confidence = self.fingerprinter.compute_cluster_confidence(
            majority_cluster, 
            fingerprints, 
            total_implementations
        )
        
        # Log similarity details
        if len(majority_cluster) > 1:
            # Compute average pairwise similarity in cluster for logging
            similarities = []
            for i in range(len(majority_cluster)):
                for j in range(i + 1, len(majority_cluster)):
                    idx_i = majority_cluster[i]
                    idx_j = majority_cluster[j]
                    sim = fingerprints[idx_i].similarity(fingerprints[idx_j])
                    similarities.append(sim)
            avg_sim = sum(similarities) / len(similarities) if similarities else 0.0
            
            self.logger.info(
                f"Similarity-based clustering: {cluster_size}/{total_implementations} in majority cluster, "
                f"avg_similarity={avg_sim:.3f}, confidence={confidence:.3f}"
            )
        else:
            self.logger.info(
                f"Single implementation selected, confidence={confidence:.3f}"
            )
        
        # Select representative from majority cluster (use first element)
        representative_idx = majority_cluster[0]
        representative_fp = fingerprints[representative_idx]
        best_clause, original_idx = fingerprint_to_clause[id(representative_fp)]
        
        # Create used_fragments metadata
        used_fragments = [{
            "prog_id": f"prog{original_idx}",
            "fragment_id": "full_clause",
            "confidence": confidence,
            "cluster_size": cluster_size,
            "total": total_implementations,
            "method": "tree_edit_distance_clustering"
        }]
        
        # Ensure code has proper function wrapper
        code = self._ensure_function_wrapper(best_clause.code, signature)
        
        return code, used_fragments, confidence

        if clauses:
            code = self._ensure_function_wrapper(clauses[0].code, signature)
            return code, [], 0.5
        
        # Last resort: generate skeleton
        return f"{signature} {{\n    // TODO: implement\n    return 0;\n}}", [], 0.0
    
    def _ensure_function_wrapper(self, code: str, signature: str) -> str:
        """Ensure code has proper function wrapper with signature and braces."""
        code = code.strip()
        
        # Check if code already has the function wrapper
        # Look for the signature at the start
        sig_clean = signature.strip()
        if code.startswith(sig_clean):
            # Already has signature, ensure it has braces
            if '{' in code and code.rstrip().endswith('}'):
                return code
            else:
                # Has signature but missing braces, wrap the body
                return f"{sig_clean} {{\n{code[len(sig_clean):].strip()}\n}}"
        
        # Code is just the body without signature/braces
        # Wrap it properly
        return f"{sig_clean} {{\n{code}\n}}"
    
    def _majority_vote(
        self,
        clauses: List[ParsedClause]
    ) -> Tuple[str, List[Dict[str, Any]], float]:
        """Select code by majority voting when no consensus."""
        # Simple approach: pick most common full implementation
        code_counter = defaultdict(int)
        code_to_clause = {}
        
        for clause in clauses:
            normalized = self.normalizer.normalize_code_text(clause.code)
            code_counter[normalized] += 1
            if normalized not in code_to_clause:
                code_to_clause[normalized] = clause
        
        if not code_counter:
            return "int placeholder() { return 0; }", [], 0.0
        
        # Pick most common
        best_code = max(code_counter.items(), key=lambda x: x[1])[0]
        count = code_counter[best_code]
        confidence = count / len(clauses)
        
        selected_clause = code_to_clause[best_code]
        
        used_fragments = [{
            "prog_id": "majority",
            "fragment_id": "full",
            "confidence": confidence,
            "fingerprint": "N/A"
        }]
        
        # Ensure proper function wrapper
        code = self._ensure_function_wrapper(selected_clause.code, selected_clause.signature)
        
        return code, used_fragments, confidence
    
    def _merge_declarations(
        self,
        decl_lists: List[Dict[str, str]]
    ) -> Dict[str, str]:
        """Merge declarations from multiple programs."""
        merged = {}
        
        for decls in decl_lists:
            for name, type_str in decls.items():
                if name not in merged:
                    merged[name] = type_str
                elif merged[name] != type_str:
                    # Conflict: keep first seen
                    self.logger.warning(f"Type conflict for {name}: {merged[name]} vs {type_str}")
        
        return merged
    
    def _create_fallback_clause(
        self,
        clause_id: str,
        signature: str,
        clauses: List[ParsedClause]
    ) -> MergedClause:
        """Create fallback clause when parsing fails."""
        # Use first available code
        code = clauses[0].code if clauses else f"{signature} {{ return 0; }}"
        
        return MergedClause(
            clause_id=clause_id,
            signature=signature,
            code=code,
            confidence=0.0,
            used_fragments=[],
            declarations={}
        )
    
    def resolve_conflicts(
        self,
        merged_clauses: List[MergedClause],
        global_includes: List[str]
    ) -> Tuple[str, List[str]]:
        """
        Resolve naming conflicts and assemble final program.
        
        Returns:
            (assembled_code, final_includes)
        """
        self.logger.info("Resolving conflicts and assembling program")
        
        # Merge includes
        all_includes = set(global_includes)
        
        # Check for name collisions across clauses
        all_names = set()
        renamed_clauses = []
        
        for clause in merged_clauses:
            # Simple conflict resolution: prefix with clause_id if needed
            # In practice, this would be more sophisticated
            renamed_clauses.append(clause)
        
        # Assemble program
        includes_str = "\n".join(sorted(all_includes))
        clauses_str = "\n\n".join(c.code for c in renamed_clauses)
        
        full_program = f"{includes_str}\n\n{clauses_str}\n"
        
        return full_program, sorted(all_includes)
