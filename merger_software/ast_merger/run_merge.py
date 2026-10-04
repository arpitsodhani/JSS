#!/usr/bin/env python3
"""
Run the AST merger on a local solutions.json and emit merged.c + confidence_report.json.
"""

import argparse
import json
import sys
from pathlib import Path

from tools.merge_c_ensemble import MergeEngine
from tools.utils import setup_logging


def build_confidence_report(merge_report_path: Path, output_path: Path) -> None:
    with merge_report_path.open("r") as f:
        merge_report = json.load(f)

    clauses = merge_report.get("clauses", {})
    clause_wise = {}
    total_conf = 0.0

    for name, data in clauses.items():
        conf = data.get("confidence", 0.0)
        num_versions = data.get("num_versions", 5)
        clause_wise[name] = {
            "confidence_score": conf,
            "cluster_info": {
                "programs_in_consensus": int(conf * num_versions),
                "total_programs": num_versions,
            },
        }
        total_conf += conf

    confidence_report = {
        "clause_wise_confidence": clause_wise,
        "overall_metrics": {
            "average_confidence": total_conf / len(clauses) if clauses else 0.0,
            "total_clauses": len(clauses),
        },
    }

    with output_path.open("w") as f:
        json.dump(confidence_report, f, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run AST merger on solutions.json")
    parser.add_argument("--input", default="solutions.json", help="Path to solutions.json")
    parser.add_argument("--out", default="merged.c", help="Output merged C file")
    parser.add_argument("--merge-report", default="merge_report.json", help="Output merge report JSON")
    parser.add_argument(
        "--confidence-report",
        default="confidence_report.json",
        help="Output confidence report JSON",
    )
    parser.add_argument("--threshold", type=float, default=0.6, help="Consensus threshold")
    parser.add_argument("--max-rounds", type=int, default=3, help="Max repair rounds")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging")
    args = parser.parse_args()

    logger = setup_logging(verbose=args.verbose)

    config = {
        "mode": "local",
        "threshold": args.threshold,
        "max_rounds": args.max_rounds,
    }

    engine = MergeEngine(config)
    success = engine.run(args.input, args.out, args.merge_report)

    merge_report_path = Path(args.merge_report)
    if not merge_report_path.exists():
        logger.error("merge_report.json not found; cannot create confidence_report.json")
        return 1

    build_confidence_report(merge_report_path, Path(args.confidence_report))

    if not success:
        logger.warning("Merge completed with errors; confidence_report.json still generated")
        return 1

    logger.info("Generated merged.c and confidence_report.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
