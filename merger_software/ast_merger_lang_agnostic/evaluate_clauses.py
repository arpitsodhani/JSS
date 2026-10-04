#!/usr/bin/env python3
"""
Main CLI tool for evaluating and merging language-agnostic code ensembles.

Usage:
    python evaluate_clauses.py --lang python --input <input.json> --out <output.py>
"""

import argparse
import sys
import os
import json
import logging

from tools.parser_base import create_parser, ParsedClause, ASTNode
from tools.normalize import normalize_clause, ASTNormalizer
from tools.fingerprint import Fingerprinter
from tools.composer import Composer


def setup_logging(verbose: bool = False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    return logging.getLogger("uast_evaluator")

class EvaluationEngine:
    def __init__(self, config):
        self.config = config
        self.lang = config["lang"]
        self.logger = logging.getLogger("uast_evaluator.engine")
        
        self.parser = create_parser(self.lang)
        self.normalizer = ASTNormalizer(self.lang)
        self.composer = Composer(lang=self.lang, threshold=config.get("threshold"))
        self.fingerprinter = Fingerprinter(self.lang)
        
        self.print_trees = config.get("print_trees", False)
        self.out_trees_file = config.get("out_trees", None)
        
        self.input_data = None
        self.parsed_programs = []
        self.merged_clauses = []
        self.final_program = ""
        self.report = {"clauses": {}}
        
    def load_input(self, file_path):
        with open(file_path, "r") as f:
            self.input_data = json.load(f)
        self.logger.info(f"Loaded {len(self.input_data.get('programs', []))} programs")
        
    def _dump_ast(self, node: ASTNode, prefix: str = "", is_last: bool = True) -> str:
        if not node: return ""
        
        # Build the current node string with box-drawing characters
        marker = "└── " if is_last else "├── "
        token_str = f" [{node.token}]" if node.token else ""
        res = f"{prefix}{marker}{node.kind}{token_str}\n"
        
        # Prepare prefix for children
        child_prefix = prefix + ("    " if is_last else "│   ")
        
        for i, child in enumerate(node.children):
            is_child_last = (i == len(node.children) - 1)
            res += self._dump_ast(child, child_prefix, is_child_last)
            
        return res

    def parse_programs(self):
        self.logger.info(f"Parsing programs for language {self.lang}...")
        
        tree_output_str = ""
        
        for prog in self.input_data.get("programs", []):
            prog_id = prog.get("id", "unknown")
            parsed_clauses = []
            
            if self.print_trees or self.out_trees_file:
                block = f"\n================ Program {prog_id} ================\n"
                if self.print_trees: print(block, end="")
                tree_output_str += block
                
            for clause_data in prog.get("clauses", []):
                # Parse
                parsed = self.parser.parse_clause(clause_data)
                
                # Normalize BEFORE printing and evaluation to see the abstracted tree
                if parsed.ast:
                    parsed.ast = self.normalizer.normalize_ast(parsed.ast)
                    
                parsed_clauses.append(parsed)
                
                if (self.print_trees or self.out_trees_file) and parsed.ast:
                    fp = self.fingerprinter.compute_fingerprint(parsed.ast, normalize=True)
                    tree_str = f"--- Clause {parsed.clause_id} AST ---\n"
                    tree_str += self._dump_ast(parsed.ast)
                    tree_str += f"Normalized Sequence Path:\n" + " -> ".join(fp.node_sequence) + "\n"
                    tree_str += "-" * 40 + "\n"
                    
                    if self.print_trees: print(tree_str, end="")
                    tree_output_str += tree_str
                    
            self.parsed_programs.append({
                "id": prog_id,
                "clauses": parsed_clauses,
                "includes": prog.get("includes", [])
            })
            
        if self.out_trees_file and tree_output_str:
            with open(self.out_trees_file, "w") as f:
                f.write(tree_output_str)
            self.logger.info(f"Wrote AST trees to {self.out_trees_file}")
            
    def evaluate_and_merge(self):
        from collections import defaultdict
        clause_groups = defaultdict(list)
        for prog in self.parsed_programs:
            for clause in prog["clauses"]:
                clause_groups[clause.clause_id].append(clause)
                
        for clause_id, variants in clause_groups.items():
            self.logger.info(f"Evaluating clause {clause_id} ({len(variants)} variants)")
            merged = self.composer.merge_clause(clause_id, variants)
            self.merged_clauses.append(merged)
            
            self.report["clauses"][clause_id] = {
                "confidence": merged.confidence,
                "agreement": getattr(merged, "agreement", 1.0),
                "used_fragments": merged.used_fragments,
                "num_versions": len(variants)
            }
            
    def assemble(self):
        self.logger.info("Assembling final code...")
        all_includes = self.input_data.get("global_includes", [])
        for prog in self.parsed_programs:
            all_includes.extend(prog.get("includes", []))
            
        # Deduplicate includes preserving order roughly
        unique_includes = list(dict.fromkeys(all_includes))
        
        self.final_program, _ = self.composer.resolve_conflicts(self.merged_clauses, unique_includes)
        
    def print_report(self):
        print("\n--- Evaluation Report ---")
        avg_confidence = sum(c["confidence"] for c in self.report["clauses"].values()) / max(1, len(self.report["clauses"]))
        print(f"Total Clauses Evaluated: {len(self.merged_clauses)}")
        print(f"Average Confidence: {avg_confidence:.2f}")
        print(f"Clustering threshold: {self.composer.threshold:.2f}")
        for cid, details in self.report["clauses"].items():
            print(f"  Clause {cid}: confidence {details['confidence']:.2f} "
                  f"agreement {details['agreement']:.3f} (from {details['used_fragments']})")

    def run(self, input_file, output_file):
        try:
            self.load_input(input_file)
            self.parse_programs()
            self.evaluate_and_merge()
            self.assemble()
            self.print_report()
            
            with open(output_file, "w") as f:
                f.write(self.final_program)
                
            self.logger.info(f"Success! Output written to {output_file}")
            return True
        except Exception as e:
            self.logger.error(f"Evaluation failed: {e}")
            return False

def main():
    parser = argparse.ArgumentParser(description="Language Agnostic UAST Evaluator")
    parser.add_argument("--lang", required=True, choices=["c", "python", "java", "javascript", "cpp"], help="Target programming language")
    parser.add_argument("--input", required=True, help="Input JSON file containing AST variants")
    parser.add_argument("--out", default="merged_output.txt", help="Output file")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    
    parser.add_argument("--threshold", type=float, default=None,
                        help="Clause clustering similarity threshold (default: per-language, 0.60 for python)")
    parser.add_argument("--print-trees", action="store_true", help="Print parsed AST trees of candidate clauses to stdout")
    parser.add_argument("--out-trees", help="Output file to write parsed AST trees to")
    
    args = parser.parse_args()
    logger = setup_logging(args.verbose)
    
    config = {
        "lang": args.lang,
        "threshold": args.threshold,
        "print_trees": args.print_trees,
        "out_trees": args.out_trees
    }
    engine = EvaluationEngine(config)
    success = engine.run(args.input, args.out)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
