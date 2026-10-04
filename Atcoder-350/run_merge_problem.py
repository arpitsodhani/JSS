#!/usr/bin/env python3
"""
Run the AST merger for a single problem folder that contains solutions.json.
Creates merged.c, merge_report.json, and confidence_report.json in that folder.
"""

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from tools.merge_c_ensemble import MergeEngine
from tools.utils import setup_logging


def build_confidence_report(merge_report_path: Path, output_path: Path) -> None:
    with merge_report_path.open("r", encoding="utf-8") as f:
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

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(confidence_report, f, indent=2)


def resolve_problem_dir(base_dir: Path, problem: str) -> Path:
    candidate = Path(problem)
    if not candidate.is_absolute():
        candidate = base_dir / candidate
    return candidate


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run AST merger on a problem folder containing solutions.json"
    )
    parser.add_argument(
        "problem",
        help="Problem directory name (relative) or absolute path",
    )
    parser.add_argument(
        "--input",
        default="solutions.json",
        help="Input file name inside the problem folder",
    )
    parser.add_argument(
        "--out",
        default="merged.c",
        help="Output merged C filename",
    )
    parser.add_argument(
        "--merge-report",
        default="merge_report.json",
        help="Output merge report JSON filename",
    )
    parser.add_argument(
        "--confidence-report",
        default="confidence_report.json",
        help="Output confidence report JSON filename",
    )
    parser.add_argument("--threshold", type=float, default=0.6, help="Consensus threshold")
    parser.add_argument("--max-rounds", type=int, default=3, help="Max repair rounds")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging")
    args = parser.parse_args()

    logger = setup_logging(verbose=args.verbose)

    problem_dir = resolve_problem_dir(SCRIPT_DIR, args.problem)
    if not problem_dir.exists() or not problem_dir.is_dir():
        logger.error("Problem directory not found: %s", problem_dir)
        return 1

    input_path = problem_dir / args.input
    if not input_path.exists():
        logger.error("Input file not found: %s", input_path)
        return 1

    out_path = problem_dir / args.out
    merge_report_path = problem_dir / args.merge_report
    confidence_report_path = problem_dir / args.confidence_report

    config = {
        "mode": "local",
        "threshold": args.threshold,
        "max_rounds": args.max_rounds,
    }

    engine = MergeEngine(config)
    success = engine.run(str(input_path), str(out_path), str(merge_report_path))

    if not merge_report_path.exists():
        logger.error("merge_report.json not found; cannot create confidence_report.json")
        return 1

    build_confidence_report(merge_report_path, confidence_report_path)

    if not success:
        logger.warning("Merge completed with errors; confidence report still generated")
        return 1

    logger.info("Generated %s and %s", out_path.name, confidence_report_path.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
