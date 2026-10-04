#!/usr/bin/env python3
"""
Main CLI tool for merging C program ensembles.

Usage:
    python merge_c_ensemble.py --input <input.json> --out <output.c> --report <report.json>
"""

import argparse
import sys
import os
import logging
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.utils import (
    setup_logging, load_json, save_json, save_text,
    validate_input_schema, create_report_template,
    merge_includes
)
from tools.parser_libclang import LibClangParser, ParsedClause
from tools.parser_treesitter import TreeSitterParser
from tools.normalize import ASTNormalizer
from tools.fingerprint import Fingerprinter
from tools.composer import Composer, MergedClause
from tools.verifier import Verifier


class MergeEngine:
    """Main engine for merging C program ensembles."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger("ast_merger.engine")
        
        # Initialize components
        self.parser = self._create_parser()
        self.normalizer = ASTNormalizer()
        self.fingerprinter = Fingerprinter()
        self.composer = Composer(threshold=config.get("threshold", 0.6))
        self.verifier = Verifier(mode=config.get("mode", "local"))
        
        # State
        self.input_data = None
        self.parsed_programs = []
        self.merged_clauses = []
        self.final_program = ""
        self.report = create_report_template()
    
    def _create_parser(self):
        """Create parser (try libclang first, fallback to tree-sitter)."""
        try:
            from tools.parser_libclang import create_parser
            self.logger.info("Using libclang parser")
            return create_parser()
        except ImportError:
            try:
                from tools.parser_treesitter import create_parser
                self.logger.info("Using tree-sitter parser (fallback)")
                return create_parser()
            except ImportError:
                self.logger.error("No parser available!")
                raise ImportError("Neither libclang nor tree-sitter is available")
    
    def load_input(self, input_file: str) -> None:
        """Load and validate input JSON."""
        self.logger.info(f"Loading input from {input_file}")
        self.input_data = load_json(input_file)
        validate_input_schema(self.input_data)
        self.logger.info(f"Loaded {len(self.input_data['programs'])} programs")
    
    def parse_programs(self) -> None:
        """Parse all programs."""
        self.logger.info("Parsing programs...")
        
        for prog in self.input_data["programs"]:
            prog_id = prog["id"]
            self.logger.info(f"Parsing program {prog_id}")
            
            parsed_clauses = []
            includes = prog.get("includes", [])
            for clause_data in prog["clauses"]:
                parsed = self.parser.parse_clause(clause_data, includes=includes)
                parsed_clauses.append(parsed)
                
                if parsed.error:
                    self.logger.warning(f"Parse error in {prog_id}/{parsed.clause_id}: {parsed.error}")
            
            self.parsed_programs.append({
                "id": prog_id,
                "clauses": parsed_clauses,
                "includes": prog.get("includes", [])
            })
        
        self.logger.info(f"Parsed {len(self.parsed_programs)} programs")
    
    def merge_clauses(self) -> None:
        """Merge clauses across programs."""
        self.logger.info("Merging clauses...")
        
        # Group clauses by clause_id
        clause_groups = defaultdict(list)
        for prog in self.parsed_programs:
            for clause in prog["clauses"]:
                clause_groups[clause.clause_id].append(clause)
        
        # Merge each group
        for clause_id, clauses in clause_groups.items():
            self.logger.info(f"Merging clause {clause_id} ({len(clauses)} versions)")
            merged = self.composer.merge_clause(clause_id, clauses)
            self.merged_clauses.append(merged)
            
            # Update report
            self.report["clauses"][clause_id] = {
                "confidence": merged.confidence,
                "used_fragments": merged.used_fragments,
                "num_versions": len(clauses)
            }
        
        self.logger.info(f"Merged {len(self.merged_clauses)} clauses")
    
    def assemble_program(self) -> None:
        """Assemble final merged program."""
        self.logger.info("Assembling final program...")
        
        # Get global includes
        global_includes = self.input_data.get("global_includes", [])
        
        # Get program includes
        prog_includes = []
        for prog in self.parsed_programs:
            prog_includes.extend(prog["includes"])
        
        # Merge includes
        all_includes = merge_includes([global_includes, prog_includes])
        
        # Resolve conflicts and assemble
        self.final_program, final_includes = self.composer.resolve_conflicts(
            self.merged_clauses,
            all_includes
        )
        
        self.logger.info("Program assembled successfully")
    
    def verify_and_repair(self, max_rounds: int = 3) -> None:
        """Verify program and attempt repairs."""
        self.logger.info("Starting verification and repair loop...")
        
        for round_num in range(max_rounds):
            self.logger.info(f"Verification round {round_num + 1}/{max_rounds}")
            
            # Compile
            compile_result = self.verifier.compile(self.final_program, "merged_program.out")
            
            # Update report
            self.report["compile_status"] = {
                "exit_code": compile_result.exit_code,
                "stdout": compile_result.stdout,
                "stderr": compile_result.stderr
            }
            
            if compile_result.success:
                self.logger.info("✓ Compilation successful")
                
                # Run tests if available
                tests = self.input_data.get("tests", {}).get("program_tests", [])
                if tests and compile_result.executable_path:
                    test_results = self.verifier.run_tests(compile_result.executable_path, tests)
                    
                    passed = sum(1 for t in test_results if t.passed)
                    total = len(test_results)
                    
                    self.report["test_results"] = {
                        "passed": passed,
                        "total": total,
                        "details": [
                            {
                                "test_id": t.test_id,
                                "passed": t.passed,
                                "expected": t.expected,
                                "actual": t.actual,
                                "error": t.error
                            }
                            for t in test_results
                        ]
                    }
                    
                    self.logger.info(f"Tests: {passed}/{total} passed")
                    
                    if passed == total:
                        self.logger.info("✓ All tests passed")
                        break
                else:
                    self.logger.info("No tests to run")
                    break
            else:
                self.logger.warning(f"✗ Compilation failed")
                
                # Analyze failures
                diagnostics = self.verifier.analyze_failures(compile_result)
                self.logger.warning(f"Diagnostics: {diagnostics}")
                
                # Attempt simple repairs
                if round_num < max_rounds - 1:
                    self.logger.info("Attempting repair...")
                    repaired = self._attempt_repair(compile_result.stderr)
                    if not repaired:
                        self.logger.warning("Could not auto-repair, stopping")
                        break
                else:
                    self.logger.warning("Max repair rounds reached")
    
    def _attempt_repair(self, stderr: str) -> bool:
        """Attempt simple repairs based on compiler errors."""
        # Simple repair strategies
        
        # Add common includes if missing
        if "implicit declaration" in stderr or "undeclared" in stderr:
            self.logger.info("Adding common includes...")
            common_includes = [
                "#include <stdio.h>",
                "#include <stdlib.h>",
                "#include <string.h>"
            ]
            
            for inc in common_includes:
                if inc not in self.final_program:
                    self.final_program = inc + "\n" + self.final_program
            
            return True
        
        return False
    
    def compute_metrics(self) -> None:
        """Compute final metrics."""
        self.logger.info("Computing metrics...")
        
        total_fragments = sum(
            len(clause["used_fragments"])
            for clause in self.report["clauses"].values()
        )
        
        avg_confidence = sum(
            clause["confidence"]
            for clause in self.report["clauses"].values()
        ) / len(self.report["clauses"]) if self.report["clauses"] else 0.0
        
        self.report["metrics"] = {
            "total_clauses": len(self.merged_clauses),
            "total_fragments": total_fragments,
            "average_confidence": avg_confidence,
            "compile_success": self.report["compile_status"]["exit_code"] == 0
        }
        
        self.logger.info(f"Metrics: {self.report['metrics']}")
    
    def save_outputs(self, output_file: str, report_file: str) -> None:
        """Save merged program and report."""
        self.logger.info(f"Saving outputs...")
        
        # Save merged program
        save_text(self.final_program, output_file)
        self.logger.info(f"✓ Saved merged program to {output_file}")
        
        # Update report with output file
        self.report["merged_program_file"] = output_file
        
        # Save report
        save_json(self.report, report_file)
        self.logger.info(f"✓ Saved merge report to {report_file}")
    
    def run(self, input_file: str, output_file: str, report_file: str) -> bool:
        """Run complete merge pipeline."""
        try:
            self.load_input(input_file)
            self.parse_programs()
            self.merge_clauses()
            self.assemble_program()
            self.verify_and_repair(max_rounds=self.config.get("max_rounds", 3))
            self.compute_metrics()
            self.save_outputs(output_file, report_file)
            
            success = self.report["compile_status"]["exit_code"] == 0
            
            if success:
                self.logger.info("✓ Merge completed successfully")
            else:
                self.logger.warning("⚠ Merge completed with compilation errors")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Fatal error: {e}", exc_info=True)
            return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Merge C program ensembles using AST analysis"
    )
    
    parser.add_argument(
        "--input",
        required=True,
        help="Input JSON file with 5 programs"
    )
    
    parser.add_argument(
        "--out",
        default="merged_program.c",
        help="Output merged C program file (default: merged_program.c)"
    )
    
    parser.add_argument(
        "--report",
        default="merge_report.json",
        help="Output merge report JSON (default: merge_report.json)"
    )
    
    parser.add_argument(
        "--mode",
        choices=["local", "docker", "judge0"],
        default="local",
        help="Verification mode (default: local)"
    )
    
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.6,
        help="Consensus threshold 0.0-1.0 (default: 0.6)"
    )
    
    parser.add_argument(
        "--max-rounds",
        type=int,
        default=3,
        help="Maximum repair rounds (default: 3)"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(verbose=args.verbose)
    
    logger.info("=" * 60)
    logger.info("C AST Ensemble Merger")
    logger.info("=" * 60)
    
    # Create config
    config = {
        "mode": args.mode,
        "threshold": args.threshold,
        "max_rounds": args.max_rounds
    }
    
    # Run merge
    engine = MergeEngine(config)
    success = engine.run(args.input, args.out, args.report)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
