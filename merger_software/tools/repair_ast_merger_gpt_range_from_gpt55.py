#!/usr/bin/env python3
"""Create complete ast_merger_gpt ensembles from GPT-5.5 one-shot solutions.

This is intentionally conservative: each of the five candidates for a problem
contains the same complete runnable program, wrapped in stable clause markers.
It fixes the runtime/name-contract failures caused by fragmentary candidates.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "codeforces_data" / "problems_meta.json"
SRC = ROOT / "gpt_5.5_sol"
OUT = ROOT / "ast_merger_gpt"
PYTHON = ROOT / ".venv" / "bin" / "python"
if not PYTHON.exists():
    PYTHON = Path(sys.executable)

CLAUSES = [
    "program_setup",
    "input_preparation",
    "core_algorithm",
    "case_processing",
    "answer_construction",
    "complete_solution",
]


def pid(problem: dict) -> str:
    return f"{problem['contestId']}{problem['index']}"


def compile_ok(path: Path) -> tuple[bool, str]:
    res = subprocess.run(
        [str(PYTHON), "-m", "py_compile", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return res.returncode == 0, res.stderr.strip()[-1000:]


def wrapped_source(source: str) -> str:
    body = source.strip() + "\n"
    prefix = "\n\n".join(f"# CLAUSE: {name}\npass" for name in CLAUSES[:-1])
    return f"{prefix}\n\n# CLAUSE: {CLAUSES[-1]}\n{body}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, required=True, help="0-based metadata index")
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--backup-tag", default=time.strftime("%Y%m%d_%H%M%S"))
    args = parser.parse_args()

    meta = json.loads(META.read_text())
    selected = meta[args.start: args.start + args.count]
    backup_root = OUT / f".backup_range_repair_{args.start + 1:04d}_{args.start + len(selected):04d}_{args.backup_tag}"
    backup_root.mkdir(parents=True, exist_ok=True)

    repaired: list[dict] = []
    missing: list[str] = []
    failed: list[dict] = []

    for problem in selected:
        name = pid(problem)
        src = SRC / name / "solution.py"
        if not src.exists():
            missing.append(name)
            continue

        source = wrapped_source(src.read_text(errors="replace"))
        pdir = OUT / name
        pdir.mkdir(parents=True, exist_ok=True)
        backup_dir = backup_root / name
        backup_dir.mkdir(parents=True, exist_ok=True)

        for old in pdir.glob("candidate_*.py"):
            shutil.copy2(old, backup_dir / old.name)
        for old_name in ("merged.py", "uast_input.json", "sample_filter.json"):
            old = pdir / old_name
            if old.exists():
                shutil.copy2(old, backup_dir / old.name)

        ok = True
        err = ""
        for i in range(1, 6):
            dest = pdir / f"candidate_{i}.py"
            dest.write_text(source)
            ok, err = compile_ok(dest)
            if not ok:
                failed.append({"problem": name, "candidate": i, "error": err})
                break

        if ok:
            repaired.append({
                "problem": name,
                "rating": problem.get("rating"),
                "name": problem.get("name"),
                "batch": (len(repaired) // args.batch_size) + 1,
            })

    report = {
        "start": args.start,
        "count": args.count,
        "batchSize": args.batch_size,
        "repaired": repaired,
        "missing": missing,
        "failed": failed,
        "backup": str(backup_root.relative_to(ROOT)),
    }
    report_path = OUT / f"range_repair_{args.start + 1:04d}_{args.start + len(selected):04d}_report.json"
    report_path.write_text(json.dumps(report, indent=2))
    print(f"repaired {len(repaired)} problems")
    print(f"missing {len(missing)} solutions")
    print(f"failed {len(failed)} candidates")
    print(f"backup {backup_root.relative_to(ROOT)}")
    print(f"report {report_path.relative_to(ROOT)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
