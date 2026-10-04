#!/usr/bin/env python3
"""
AST composer logic to merge clauses.
"""
import logging
from typing import Dict, List, Tuple
from dataclasses import dataclass

from tools.parser_base import ParsedClause
from tools.fingerprint import Fingerprinter, ASTFingerprint

@dataclass
class MergedClause:
    clause_id: str
    code: str
    confidence: float
    used_fragments: List[str]
    agreement: float = 1.0

class Composer:
    """Composer merges language-agnostic sub-ast strings by clustering tree-edit distance representations."""
    
    def __init__(self, lang: str, threshold: float = None):
        self.logger = logging.getLogger("ast_merger.composer")
        self.lang = lang
        self.fingerprinter = Fingerprinter(lang)
        # Previously self.threshold was stored and then ignored: merge_clause
        # clustered at a hardcoded 0.7 regardless of what was configured. The
        # configured value now actually reaches the clustering step, and the
        # default comes from the language config rather than a magic number.
        if threshold is None:
            threshold = self.fingerprinter.config.get("cluster_threshold", 0.60)
        self.threshold = threshold
    
    def merge_clause(self, clause_id: str, clauses: List[ParsedClause]) -> MergedClause:
        """Find the consensus clause from multiple variants."""
        if not clauses:
            return MergedClause(clause_id="unknown", code="", confidence=0.0, used_fragments=[])
            
        if len(clauses) == 1:
            return MergedClause(
                clause_id=clause_id,
                code=clauses[0].code,
                confidence=1.0,
                used_fragments=["single_variant"]
            )
        
        fingerprints = []
        for c in clauses:
            fp = self.fingerprinter.compute_fingerprint(c.ast)
            fingerprints.append(fp)
            
        # Cluster signatures with relatively high structural similarity
        clusters = self.fingerprinter.cluster_fingerprints(fingerprints, similarity_threshold=self.threshold)
        
        # Sort clusters by size
        clusters.sort(key=len, reverse=True)
        largest_cluster = clusters[0]
        
        # In a real tool, compute average internal similarity of largest cluster
        # Then (len(largest) / total) * internal_sim
        confidence = (len(largest_cluster) / len(clauses)) if clauses else 0.0

        medoid_idx = self._cluster_medoid(largest_cluster, fingerprints, clauses)
        selected_clause = clauses[medoid_idx]

        merged = MergedClause(
            clause_id=clause_id,
            code=selected_clause.code,
            confidence=confidence,
            used_fragments=[f"prog_{i}" for i in largest_cluster]
        )
        merged.agreement = self._cluster_agreement(largest_cluster, fingerprints)
        return merged

    def _cluster_agreement(self, cluster: List[int], fingerprints: List[ASTFingerprint]) -> float:
        """Mean pairwise similarity inside the winning cluster.

        confidence is quantised to k/n (with 5 variants it can only be 0.2, 0.4,
        0.6, 0.8, 1.0), so it says nothing about *how* strongly the cluster
        agrees. This continuous companion does.
        """
        if len(cluster) < 2:
            return 1.0
        total = 0.0
        pairs = 0
        for a in range(len(cluster)):
            for b in range(a + 1, len(cluster)):
                total += fingerprints[cluster[a]].similarity(fingerprints[cluster[b]])
                pairs += 1
        return total / pairs if pairs else 1.0

    def _cluster_medoid(self, cluster: List[int], fingerprints: List[ASTFingerprint],
                        clauses: List[ParsedClause] = None) -> int:
        """Choose the variant most similar to the rest of its cluster.

        Ties used to be broken by whichever index was seen first, so permuting
        the programs in the input file could change which variant was emitted
        even though the clustering was identical. Ties now break on the
        structural key and then the clause text, both of which are properties of
        the code rather than of its position in the input.
        """
        if len(cluster) == 1:
            return cluster[0]

        scored = []
        for idx in cluster:
            score = 0.0
            for other_idx in cluster:
                if idx == other_idx:
                    continue
                score += fingerprints[idx].similarity(fingerprints[other_idx])
            score /= max(1, len(cluster) - 1)
            key = getattr(fingerprints[idx], "structural_key", "") or ""
            text = clauses[idx].code if clauses else ""
            scored.append((-round(score, 9), key, text, idx))
        scored.sort()
        return scored[0][3]
    
    def resolve_conflicts(self, merged_clauses: List[MergedClause], includes: List[str] = None) -> Tuple[str, List[str]]:
        """Assemble the complete program from its consensus clauses."""
        final_code = ""
        
        if includes:
            final_code += "\n".join(includes)
            final_code += "\n\n"
        
        # Concatenate selected clauses for target language
        for clause in merged_clauses:
            if self.lang == "python":
                final_code += f"# Clause {clause.clause_id} [Confidence: {clause.confidence:.2f}]\n"
            else:
                final_code += f"/* Clause {clause.clause_id} [Confidence: {clause.confidence:.2f}] */\n"
            final_code += clause.code + "\n\n"
            
        return final_code, includes or []
