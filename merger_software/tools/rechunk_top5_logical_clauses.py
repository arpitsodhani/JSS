#!/usr/bin/env python3
"""Regenerate ast_merger_gpt candidates with real multi-clause sections.

This script reads gpt_5.5_sol/<pid>/solution.py, normalizes it with Python's AST,
groups actual top-level statements into contiguous logical clauses, writes five
complete candidates with the same clause layout, and leaves one-clause programs
only when the normalized program has no safe split point.
"""
from __future__ import annotations

import argparse
import ast
import builtins
import copy
import json
import keyword
import re
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

PLACEHOLDER_RE = re.compile(
    r"(?im)^\s*pass\s*(?:#.*)?$|todo\b|fixme\b|placeholder\b|stub\b|"
    r"not\s+implemented|left\s+to\s+implement|implement\s+me"
)
RESERVED = set(dir(builtins)) | set(keyword.kwlist)


def problem_id(problem: dict) -> str:
    return f"{problem['contestId']}{problem['index']}"


def strip_module_docstring(tree: ast.Module) -> ast.Module:
    if (
        tree.body
        and isinstance(tree.body[0], ast.Expr)
        and isinstance(tree.body[0].value, ast.Constant)
        and isinstance(tree.body[0].value.value, str)
    ):
        tree.body = tree.body[1:]
    return tree


def is_main_guard(node: ast.AST) -> bool:
    if not isinstance(node, ast.If):
        return False
    test = node.test
    return (
        isinstance(test, ast.Compare)
        and isinstance(test.left, ast.Name)
        and test.left.id == "__name__"
        and len(test.ops) == 1
        and isinstance(test.ops[0], ast.Eq)
        and len(test.comparators) == 1
        and isinstance(test.comparators[0], ast.Constant)
        and test.comparators[0].value == "__main__"
    )


def contains_input_call(node: ast.AST) -> bool:
    for sub in ast.walk(node):
        if isinstance(sub, ast.Call):
            fn = sub.func
            if isinstance(fn, ast.Name) and fn.id == "input":
                return True
            if isinstance(fn, ast.Attribute) and fn.attr in {"read", "readline", "readlines"}:
                base = fn.value
                if isinstance(base, ast.Attribute) and base.attr in {"stdin", "buffer"}:
                    return True
                if isinstance(base, ast.Name) and base.id in {"stdin", "input"}:
                    return True
        if isinstance(sub, ast.Name) and sub.id in {"stdin"}:
            return True
    return False


def contains_output_call(node: ast.AST) -> bool:
    for sub in ast.walk(node):
        if isinstance(sub, ast.Call):
            fn = sub.func
            if isinstance(fn, ast.Name) and fn.id == "print":
                return True
            if isinstance(fn, ast.Attribute) and fn.attr in {"write", "writelines"}:
                return True
    return False


def classify(node: ast.AST) -> str:
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        return "setup_imports"
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return "define_helpers"
    if is_main_guard(node):
        return "run_solution"
    if contains_input_call(node):
        return "read_problem_data"
    if contains_output_call(node):
        return "emit_output"
    return "compute_answer"


def unique_clause_ids(labels: list[str]) -> list[str]:
    counts: dict[str, int] = {}
    out = []
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
        out.append(label if counts[label] == 1 else f"{label}_{counts[label]}")
    return out


def grouped_clauses(tree: ast.Module) -> list[tuple[str, list[ast.stmt]]]:
    if not tree.body:
        return [("complete_solution", [])]
    groups: list[tuple[str, list[ast.stmt]]] = []
    current_label = classify(tree.body[0])
    current: list[ast.stmt] = []
    for stmt in tree.body:
        label = classify(stmt)
        if current and label != current_label:
            groups.append((current_label, current))
            current = []
            current_label = label
        current.append(stmt)
    if current:
        groups.append((current_label, current))

    if len(groups) == 1 and len(tree.body) > 1:
        groups = split_single_group(groups[0])

    labels = unique_clause_ids([label for label, _ in groups])
    return [(labels[i], stmts) for i, (_, stmts) in enumerate(groups)]


def split_single_group(group: tuple[str, list[ast.stmt]]) -> list[tuple[str, list[ast.stmt]]]:
    label, stmts = group
    if len(stmts) < 2:
        return group and [group]
    n = len(stmts)
    if n == 2:
        cuts = [1]
    elif n == 3:
        cuts = [1, 2]
    else:
        cuts = [max(1, n // 3), max(2, (2 * n) // 3)]
        cuts = sorted(set(c for c in cuts if 0 < c < n))
    names = {
        "compute_answer": ["prepare_state", "apply_algorithm", "finalize_answer"],
        "read_problem_data": ["read_problem_data", "parse_case_state", "prepare_case_state"],
        "emit_output": ["prepare_output", "format_output", "emit_output"],
        "define_helpers": ["define_core_helpers", "define_algorithm_helpers", "define_driver"],
    }.get(label, [f"{label}_part_1", f"{label}_part_2", f"{label}_part_3"])
    chunks = []
    prev = 0
    for idx, cut in enumerate(cuts + [n]):
        chunks.append((names[min(idx, len(names) - 1)], stmts[prev:cut]))
        prev = cut
    return chunks


class LocalRenamer(ast.NodeTransformer):
    def __init__(self, suffix: str) -> None:
        self.suffix = suffix
        self.stack: list[dict[str, str]] = []

    def collect_mapping(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> dict[str, str]:
        assigned: set[str] = set()
        declared_global: set[str] = set()
        declared_nonlocal: set[str] = set()
        for sub in ast.walk(node):
            if sub is node:
                continue
            if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
                continue
            if isinstance(sub, ast.Global):
                declared_global.update(sub.names)
            elif isinstance(sub, ast.Nonlocal):
                declared_nonlocal.update(sub.names)
            elif isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Store):
                assigned.add(sub.id)
        args = {
            arg.arg
            for arg in node.args.posonlyargs + node.args.args + node.args.kwonlyargs
        }
        if node.args.vararg:
            args.add(node.args.vararg.arg)
        if node.args.kwarg:
            args.add(node.args.kwarg.arg)
        blocked = RESERVED | declared_global | declared_nonlocal
        return {
            name: f"{name}_{self.suffix}"
            for name in sorted(args | assigned)
            if name not in blocked and not (name.startswith("__") and name.endswith("__"))
        }

    def current(self) -> dict[str, str]:
        out: dict[str, str] = {}
        for mapping in self.stack:
            out.update(mapping)
        return out

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        mapping = self.collect_mapping(node)
        for arg in node.args.posonlyargs + node.args.args + node.args.kwonlyargs:
            arg.arg = mapping.get(arg.arg, arg.arg)
        if node.args.vararg:
            node.args.vararg.arg = mapping.get(node.args.vararg.arg, node.args.vararg.arg)
        if node.args.kwarg:
            node.args.kwarg.arg = mapping.get(node.args.kwarg.arg, node.args.kwarg.arg)
        self.stack.append(mapping)
        node.body = [self.visit(stmt) for stmt in node.body]
        self.stack.pop()
        return node

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
        return self.visit_FunctionDef(node)

    def visit_Name(self, node: ast.Name) -> ast.AST:
        node.id = self.current().get(node.id, node.id)
        return node

    def visit_Nonlocal(self, node: ast.Nonlocal) -> ast.AST:
        mapping = self.current()
        node.names = [mapping.get(name, name) for name in node.names]
        return node


def chunk_source(stmts: list[ast.stmt]) -> str:
    if not stmts:
        return ""
    return "\n".join(ast.unparse(stmt) for stmt in stmts).strip() + "\n"


def candidate_source(seed: str, variant: int) -> tuple[str, int]:
    tree = strip_module_docstring(ast.parse(seed))
    tree = copy.deepcopy(tree)
    if variant > 1:
        tree = LocalRenamer(f"v{variant}").visit(tree)
    ast.fix_missing_locations(tree)
    groups = grouped_clauses(tree)
    parts = []
    for clause_id, stmts in groups:
        body = chunk_source(stmts)
        if body:
            parts.append(f"# CLAUSE: {clause_id}\n{body}")
    if not parts:
        parts.append("# CLAUSE: complete_solution\n")
    return "\n".join(parts), len(parts)


def compile_ok(path: Path) -> tuple[bool, str]:
    res = subprocess.run(
        [str(PYTHON), "-m", "py_compile", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return res.returncode == 0, res.stderr.strip()[-1000:]


def backup_problem(pdir: Path, backup_root: Path) -> None:
    if not pdir.exists():
        return
    dest = backup_root / pdir.name
    if dest.exists():
        return
    dest.mkdir(parents=True, exist_ok=True)
    for path in pdir.iterdir():
        if path.is_file():
            shutil.copy2(path, dest / path.name)


def generate_one(pid: str, backup_root: Path) -> dict:
    src = SRC / pid / "solution.py"
    if not src.exists():
        return {"problem": pid, "status": "missing-seed"}
    seed = src.read_text(errors="replace")
    try:
        built = [candidate_source(seed, i) for i in range(1, 6)]
    except Exception as exc:
        return {"problem": pid, "status": "parse-failed", "error": str(exc)}
    codes = [code for code, _ in built]
    clause_counts = [count for _, count in built]
    if len(set(clause_counts)) != 1:
        return {"problem": pid, "status": "layout-mismatch", "clauseCounts": clause_counts}
    for i, code in enumerate(codes, 1):
        if PLACEHOLDER_RE.search(code):
            return {"problem": pid, "status": "placeholder-hit", "candidate": i}
    pdir = OUT / pid
    backup_problem(pdir, backup_root)
    pdir.mkdir(parents=True, exist_ok=True)
    for old in pdir.glob("candidate_*.py"):
        old.unlink()
    for old_name in ("merged.py", "uast_input.json", "uast_input_whole_program_fallback.json",
                     "sample_filter.json", "merge.log", "merge_fallback.log", "trees.txt"):
        (pdir / old_name).unlink(missing_ok=True)
    for i, code in enumerate(codes, 1):
        path = pdir / f"candidate_{i}.py"
        path.write_text(code if code.endswith("\n") else code + "\n")
        ok, err = compile_ok(path)
        if not ok:
            return {"problem": pid, "status": "compile-failed", "candidate": i, "error": err}
    return {
        "problem": pid,
        "status": "generated",
        "clauses": clause_counts[0],
        "uniqueText": len({code.strip() for code in codes}),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=10, help="0-based metadata start")
    parser.add_argument("--count", type=int, default=990)
    parser.add_argument("--tag", default=time.strftime("%Y%m%d_%H%M%S"))
    args = parser.parse_args()

    meta = json.loads(META.read_text())
    selected = meta[args.start:args.start + args.count]
    backup_root = OUT / f".backup_rechunk_logical_{args.start + 1:04d}_{args.start + len(selected):04d}_{args.tag}"
    backup_root.mkdir(parents=True, exist_ok=True)
    rows = []
    hist: dict[int, int] = {}
    for n, problem in enumerate(selected, 1):
        pid = problem_id(problem)
        row = generate_one(pid, backup_root)
        rows.append(row)
        if row["status"] == "generated":
            hist[row["clauses"]] = hist.get(row["clauses"], 0) + 1
        print(
            f"[rechunk {n:03d}/{len(selected):03d}] {pid}: {row['status']} "
            f"clauses={row.get('clauses', '-')} hist={dict(sorted(hist.items()))}",
            flush=True,
        )
    report = {
        "start": args.start,
        "count": len(selected),
        "backupRoot": str(backup_root.relative_to(ROOT)),
        "rows": rows,
        "counts": {
            status: sum(1 for row in rows if row["status"] == status)
            for status in sorted({row["status"] for row in rows})
        },
        "clauseHistogram": {str(k): v for k, v in sorted(hist.items())},
    }
    report_path = OUT / f"rechunk_logical_{args.start + 1:04d}_{args.start + len(selected):04d}_report.json"
    report_path.write_text(json.dumps(report, indent=2))
    print(f"report={report_path}", flush=True)
    return 0 if all(row["status"] == "generated" for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
