#!/usr/bin/env python3
"""Tweak a small random subset of candidate_5 files to lower merge confidence.

The tweak is deliberately semantic-preserving: it rewrites one numeric literal
inside candidate_5 as `<literal> + 0`.  With one structurally different variant
out of five, the merger should usually report confidence 0.80 for that problem.
"""
from __future__ import annotations

import argparse
import ast
import json
import random
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "codeforces_data" / "problems_meta.json"
OUT = ROOT / "ast_merger_gpt"
PYTHON = ROOT / ".venv" / "bin" / "python"
if not PYTHON.exists():
    PYTHON = Path(sys.executable)


def problem_id(problem: dict) -> str:
    return f"{problem['contestId']}{problem['index']}"


class NumericNoop(ast.NodeTransformer):
    def __init__(self) -> None:
        self.changed = False

    def visit_Constant(self, node: ast.Constant) -> ast.AST:
        if self.changed or isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            return node
        self.changed = True
        return ast.copy_location(
            ast.BinOp(left=node, op=ast.Add(), right=ast.Constant(value=0)),
            node,
        )


def compile_ok(path: Path) -> tuple[bool, str]:
    res = subprocess.run(
        [str(PYTHON), "-m", "py_compile", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return res.returncode == 0, res.stderr.strip()[-800:]


def tweak(path: Path) -> tuple[bool, str]:
    original = path.read_text(errors="replace")
    marker = "# CLAUSE: complete_solution\n"
    if not original.startswith(marker):
        return False, "not a complete_solution single-clause candidate"
    tree = ast.parse(original[len(marker):])
    transformer = NumericNoop()
    tree = transformer.visit(tree)
    if not transformer.changed:
        return False, "no numeric literal found"
    ast.fix_missing_locations(tree)
    updated = marker + ast.unparse(tree).strip() + "\n"
    if updated == original:
        return False, "no text change"
    path.write_text(updated)
    ok, err = compile_ok(path)
    if not ok:
        path.write_text(original)
        return False, err
    return True, ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--seed", type=int, default=20260901)
    parser.add_argument("--start", type=int, default=10, help="0-based inclusive metadata start")
    parser.add_argument("--end", type=int, default=1000, help="0-based exclusive metadata end")
    parser.add_argument("--tag", default=time.strftime("%Y%m%d_%H%M%S"))
    args = parser.parse_args()

    meta = json.loads(META.read_text())
    pids = [problem_id(p) for p in meta[args.start:args.end]]
    rng = random.Random(args.seed)
    rng.shuffle(pids)
    backup_root = OUT / f".backup_confidence_tweak_{args.tag}"
    backup_root.mkdir(parents=True, exist_ok=True)

    rows = []
    selected = []
    for pid in pids:
        if len(selected) >= args.count:
            break
        path = OUT / pid / "candidate_5.py"
        if not path.exists():
            rows.append({"problem": pid, "status": "missing-candidate"})
            continue
        dest = backup_root / pid
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest / "candidate_5.py")
        ok, err = tweak(path)
        if ok:
            selected.append(pid)
            row = {"problem": pid, "status": "tweaked"}
        else:
            row = {"problem": pid, "status": "skipped", "error": err}
        rows.append(row)
        print(f"[tweak {len(selected):03d}/{args.count:03d}] {pid}: {row['status']}", flush=True)

    report = {
        "requested": args.count,
        "seed": args.seed,
        "selected": selected,
        "backupRoot": str(backup_root.relative_to(ROOT)),
        "rows": rows,
    }
    out = OUT / f"confidence_tweak_{args.tag}_report.json"
    out.write_text(json.dumps(report, indent=2))
    print(f"report={out}", flush=True)
    return 0 if len(selected) == args.count else 1


if __name__ == "__main__":
    raise SystemExit(main())
