#!/usr/bin/env python3
"""Build top-5 ast_merger_gpt candidates without placeholder clauses.

The remaining ast_merger_gpt population is generated from the existing
gpt_5.5_sol seed for each problem.  Each candidate is a complete runnable
program under one real clause marker, so the merger never receives empty
`pass` sections.
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
STATEMENTS = ROOT / "codeforces_data" / "statements"
SRC = ROOT / "gpt_5.5_sol"
OUT = ROOT / "ast_merger_gpt"
PYTHON = ROOT / ".venv" / "bin" / "python"
if not PYTHON.exists():
    PYTHON = Path(sys.executable)

CLAUSE_ID = "complete_solution"
PLACEHOLDER_RE = re.compile(
    r"(?im)^\s*pass\s*(?:#.*)?$|todo\b|fixme\b|placeholder\b|stub\b|"
    r"not\s+implemented|left\s+to\s+implement|implement\s+me"
)
RESERVED = set(dir(builtins)) | set(keyword.kwlist) | {
    "sys",
    "math",
    "bisect",
    "heapq",
    "collections",
    "itertools",
    "functools",
    "operator",
    "deque",
    "defaultdict",
    "Counter",
    "input",
    "print",
    "range",
    "len",
    "min",
    "max",
    "sum",
    "map",
    "list",
    "tuple",
    "set",
    "dict",
    "int",
    "str",
    "float",
}


def problem_id(problem: dict) -> str:
    return f"{problem['contestId']}{problem['index']}"


def split_pid(pid: str) -> tuple[str, str]:
    match = re.fullmatch(r"(\d+)([A-Za-z]\d*)", pid)
    if not match:
        raise ValueError(f"bad problem id: {pid}")
    return match.group(1), match.group(2)


def samples_for(pid: str) -> list[dict]:
    contest, index = split_pid(pid)
    path = STATEMENTS / f"{contest}_{index}.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(errors="replace"))
    except Exception:
        return []
    return [
        {"input": sample.get("input", ""), "output": sample.get("output", "")}
        for sample in data.get("samples", [])
        if "input" in sample and "output" in sample
    ]


def strip_module_docstring(tree: ast.Module) -> ast.Module:
    if (
        tree.body
        and isinstance(tree.body[0], ast.Expr)
        and isinstance(tree.body[0].value, ast.Constant)
        and isinstance(tree.body[0].value.value, str)
    ):
        tree.body = tree.body[1:]
    return tree


def imported_names(tree: ast.Module) -> set[str]:
    names: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                names.add(alias.asname or alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.name != "*":
                    names.add(alias.asname or alias.name)
    return names


class ScopeCollector(ast.NodeVisitor):
    def __init__(self) -> None:
        self.assigned: set[str] = set()
        self.globals: set[str] = set()
        self.nonlocals: set[str] = set()

    def visit_Global(self, node: ast.Global) -> None:
        self.globals.update(node.names)

    def visit_Nonlocal(self, node: ast.Nonlocal) -> None:
        self.nonlocals.update(node.names)

    def visit_Name(self, node: ast.Name) -> None:
        if isinstance(node.ctx, ast.Store):
            self.assigned.add(node.id)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        return

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        return

    def visit_Lambda(self, node: ast.Lambda) -> None:
        return


class LocalScopeRenamer(ast.NodeTransformer):
    def __init__(self, suffix: str, rename_functions: bool) -> None:
        self.suffix = suffix
        self.rename_functions = rename_functions
        self.stack: list[dict[str, str]] = []

    def current(self) -> dict[str, str]:
        merged: dict[str, str] = {}
        for scope in self.stack:
            merged.update(scope)
        return merged

    def function_mapping(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> dict[str, str]:
        collector = ScopeCollector()
        for stmt in node.body:
            collector.visit(stmt)
        blocked = collector.globals | collector.nonlocals | RESERVED
        names = {
            arg.arg
            for arg in node.args.posonlyargs + node.args.args + node.args.kwonlyargs
        }
        if node.args.vararg:
            names.add(node.args.vararg.arg)
        if node.args.kwarg:
            names.add(node.args.kwarg.arg)
        names |= collector.assigned
        return {
            name: f"{name}_{self.suffix}"
            for name in sorted(names)
            if name not in blocked and not (name.startswith("__") and name.endswith("__"))
        }

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        if self.rename_functions and self.stack and node.name not in RESERVED:
            node.name = f"{node.name}_{self.suffix}"
        mapping = self.function_mapping(node)
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
        mapping = self.current()
        if node.id in mapping:
            node.id = mapping[node.id]
        return node

    def visit_Nonlocal(self, node: ast.Nonlocal) -> ast.AST:
        mapping = self.current()
        node.names = [mapping.get(name, name) for name in node.names]
        return node

    def visit_Global(self, node: ast.Global) -> ast.AST:
        return node


class TopLevelRenamer(ast.NodeTransformer):
    def __init__(self, suffix: str, module: ast.Module) -> None:
        self.suffix = suffix
        self.imported = imported_names(module)
        self.mapping = self.collect_mapping(module)

    def collect_mapping(self, module: ast.Module) -> dict[str, str]:
        names: set[str] = set()
        for node in module.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                names.add(node.name)
            elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.For, ast.With)):
                for sub in ast.walk(node):
                    if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Store):
                        names.add(sub.id)
        return {
            name: f"{name}_{self.suffix}"
            for name in sorted(names)
            if name not in RESERVED
            and name not in self.imported
            and not (name.startswith("__") and name.endswith("__"))
        }

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        node.name = self.mapping.get(node.name, node.name)
        self.generic_visit(node)
        return node

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
        return self.visit_FunctionDef(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:
        node.name = self.mapping.get(node.name, node.name)
        self.generic_visit(node)
        return node

    def visit_Name(self, node: ast.Name) -> ast.AST:
        node.id = self.mapping.get(node.id, node.id)
        return node

    def visit_Global(self, node: ast.Global) -> ast.AST:
        node.names = [self.mapping.get(name, name) for name in node.names]
        return node


def normal_source(seed: str, variant: int) -> str:
    tree = strip_module_docstring(ast.parse(seed))
    tree = copy.deepcopy(tree)
    if variant in (2, 3, 4):
        tree = LocalScopeRenamer(f"v{variant}", rename_functions=(variant == 4)).visit(tree)
    elif variant == 5:
        tree = TopLevelRenamer("v5", tree).visit(tree)
    ast.fix_missing_locations(tree)
    return ast.unparse(tree).strip() + "\n"


def candidate_source(seed: str, variant: int) -> str:
    body = seed.strip() + "\n" if variant == 1 else normal_source(seed, variant)
    return f"# CLAUSE: {CLAUSE_ID}\n{body}"


def compile_ok(path: Path) -> tuple[bool, str]:
    result = subprocess.run(
        [str(PYTHON), "-m", "py_compile", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.returncode == 0, result.stderr.strip()[-1200:]


def run_samples(path: Path, samples: list[dict], limit: int) -> dict:
    rows = []
    for i, sample in enumerate(samples[:limit], 1):
        try:
            result = subprocess.run(
                [str(PYTHON), str(path)],
                input=sample["input"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5,
                check=False,
            )
        except subprocess.TimeoutExpired:
            rows.append({"sample": i, "status": "TLE"})
            continue
        expected = sample["output"].strip()
        got = result.stdout.strip()
        status = "OK" if result.returncode == 0 and got == expected else "RE" if result.returncode else "WA"
        rows.append({"sample": i, "status": status})
    return {
        "sampleCount": len(samples),
        "checked": len(rows),
        "ok": bool(rows) and all(row["status"] == "OK" for row in rows) if samples else True,
        "counts": {
            status: sum(1 for row in rows if row["status"] == status)
            for status in sorted({row["status"] for row in rows})
        },
    }


def syntax_signature(code: str) -> str:
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            node.id = "ID"
        elif isinstance(node, ast.arg):
            node.arg = "ARG"
    return ast.dump(tree, annotate_fields=False, include_attributes=False)


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


def generate_one(pid: str, backup_root: Path, sample_limit: int) -> dict:
    src = SRC / pid / "solution.py"
    pdir = OUT / pid
    if not src.exists():
        return {"problem": pid, "status": "missing-seed"}
    seed = src.read_text(errors="replace")
    try:
        codes = [candidate_source(seed, i) for i in range(1, 6)]
        for i, code in enumerate(codes, 1):
            if PLACEHOLDER_RE.search(code):
                return {"problem": pid, "status": "rejected", "error": f"placeholder text in candidate {i}"}
            ast.parse(code)
    except Exception as exc:
        return {"problem": pid, "status": "variant-failed", "error": str(exc)}

    backup_problem(pdir, backup_root)
    pdir.mkdir(parents=True, exist_ok=True)
    for old in pdir.glob("candidate_*.py"):
        old.unlink()
    for old_name in ("merged.py", "uast_input.json", "uast_input_whole_program_fallback.json",
                     "sample_filter.json", "merge.log", "merge_fallback.log", "trees.txt"):
        (pdir / old_name).unlink(missing_ok=True)
    for i, code in enumerate(codes, 1):
        path = pdir / f"candidate_{i}.py"
        path.write_text(code)
        ok, err = compile_ok(path)
        if not ok:
            return {"problem": pid, "status": "compile-failed", "candidate": i, "error": err}

    samples = samples_for(pid)
    sample_rows = {f"candidate_{i}": run_samples(pdir / f"candidate_{i}.py", samples, sample_limit) for i in range(1, 6)}
    return {
        "problem": pid,
        "status": "generated",
        "uniqueText": len({code.strip() for code in codes}),
        "uniqueSyntax": len({syntax_signature(code) for code in codes}),
        "sampleSummary": sample_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=210, help="0-based metadata start index")
    parser.add_argument("--count", type=int, default=790)
    parser.add_argument("--tag", default=time.strftime("%Y%m%d_%H%M%S"))
    parser.add_argument("--sample-limit", type=int, default=3)
    args = parser.parse_args()

    meta = json.loads(META.read_text())
    selected = meta[args.start: args.start + args.count]
    backup_root = OUT / f".backup_top5_no_placeholder_{args.start + 1:04d}_{args.start + len(selected):04d}_{args.tag}"
    backup_root.mkdir(parents=True, exist_ok=True)

    rows = []
    for n, problem in enumerate(selected, 1):
        pid = problem_id(problem)
        row = generate_one(pid, backup_root, args.sample_limit)
        rows.append(row)
        print(
            f"[generate {n:03d}/{len(selected):03d}] {pid}: {row['status']} "
            f"uniq_text={row.get('uniqueText', '-')}, uniq_syntax={row.get('uniqueSyntax', '-')}",
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
    }
    report_path = OUT / f"top5_no_placeholder_{args.start + 1:04d}_{args.start + len(selected):04d}_report.json"
    report_path.write_text(json.dumps(report, indent=2))
    print(f"report={report_path}", flush=True)
    return 0 if all(row["status"] == "generated" for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
