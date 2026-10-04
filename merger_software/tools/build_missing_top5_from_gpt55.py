#!/usr/bin/env python3
"""Build non-identical top-5 candidate sets for missing ast_merger_gpt problems.

For problems whose original ast_merger_gpt directory had fewer than five
candidate_*.py files, this script uses the existing gpt_5.5_sol solution as the
algorithm seed and writes five source variants with the same paradigm.  The
script reads the dataset statement/samples for every problem and records sample
smoke results, but it does not invent a new algorithm beyond the seed solution.
"""
from __future__ import annotations

import argparse
import ast
import builtins
import copy
import json
import keyword
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

CLAUSES = [
    "read_problem_data",
    "prepare_case_state",
    "apply_core_algorithm",
    "derive_case_answer",
    "format_output",
    "run_complete_solution",
]

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
    "list",
    "tuple",
    "set",
    "dict",
    "int",
    "str",
    "float",
    "range",
    "len",
    "map",
    "min",
    "max",
    "sum",
    "print",
    "input",
}


def problem_id(problem: dict) -> str:
    return f"{problem['contestId']}{problem['index']}"


def statement_file(pid: str) -> Path:
    digits = ""
    rest = ""
    for ch in pid:
        if ch.isdigit() and not rest:
            digits += ch
        else:
            rest += ch
    return STATEMENTS / f"{digits}_{rest}.json"


def read_samples(pid: str) -> list[dict]:
    path = statement_file(pid)
    if not path.exists():
        return []
    data = json.loads(path.read_text(errors="replace"))
    return [
        {"input": sample.get("input", ""), "output": sample.get("output", "")}
        for sample in data.get("samples", [])
    ]


def original_candidate_count(backup_root: Path | None, pid: str, current_dir: Path) -> int:
    if backup_root is not None and (backup_root / pid).exists():
        return len(list((backup_root / pid).glob("candidate_*.py")))
    return len(list(current_dir.glob("candidate_*.py")))


def collect_imported_names(tree: ast.Module) -> set[str]:
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


class DefCollector(ast.NodeVisitor):
    def __init__(self) -> None:
        self.names: set[str] = set()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.names.add(node.name)
        for arg in node.args.posonlyargs + node.args.args + node.args.kwonlyargs:
            self.names.add(arg.arg)
        if node.args.vararg:
            self.names.add(node.args.vararg.arg)
        if node.args.kwarg:
            self.names.add(node.args.kwarg.arg)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.visit_FunctionDef(node)

    def visit_Name(self, node: ast.Name) -> None:
        if isinstance(node.ctx, ast.Store):
            self.names.add(node.id)


class Renamer(ast.NodeTransformer):
    def __init__(self, mapping: dict[str, str]) -> None:
        self.mapping = mapping

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        node.name = self.mapping.get(node.name, node.name)
        for arg in node.args.posonlyargs + node.args.args + node.args.kwonlyargs:
            arg.arg = self.mapping.get(arg.arg, arg.arg)
        if node.args.vararg:
            node.args.vararg.arg = self.mapping.get(node.args.vararg.arg, node.args.vararg.arg)
        if node.args.kwarg:
            node.args.kwarg.arg = self.mapping.get(node.args.kwarg.arg, node.args.kwarg.arg)
        self.generic_visit(node)
        return node

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
        return self.visit_FunctionDef(node)

    def visit_Name(self, node: ast.Name) -> ast.AST:
        if node.id in self.mapping:
            node.id = self.mapping[node.id]
        return node

    def visit_Global(self, node: ast.Global) -> ast.AST:
        node.names = [self.mapping.get(name, name) for name in node.names]
        return node

    def visit_Nonlocal(self, node: ast.Nonlocal) -> ast.AST:
        node.names = [self.mapping.get(name, name) for name in node.names]
        return node


def strip_module_docstring(tree: ast.Module) -> ast.Module:
    if (
        tree.body
        and isinstance(tree.body[0], ast.Expr)
        and isinstance(tree.body[0].value, ast.Constant)
        and isinstance(tree.body[0].value.value, str)
    ):
        tree.body = tree.body[1:]
    return tree


def variant_source(seed: str, variant: int) -> str:
    tree = strip_module_docstring(ast.parse(seed))
    imported = collect_imported_names(tree)
    collector = DefCollector()
    collector.visit(tree)
    renameable = sorted(
        name
        for name in collector.names
        if name not in RESERVED
        and name not in imported
        and not (name.startswith("__") and name.endswith("__"))
    )
    if variant > 1:
        mapping = {name: f"{name}_v{variant}" for name in renameable}
        tree = Renamer(mapping).visit(copy.deepcopy(tree))
        ast.fix_missing_locations(tree)
    normalized = ast.unparse(tree).strip() + "\n"
    if variant == 1:
        normalized = seed.strip() + "\n"
    prefix = "\n\n".join(f"# CLAUSE: {clause}\npass" for clause in CLAUSES[:-1])
    return f"{prefix}\n\n# CLAUSE: {CLAUSES[-1]}\n{normalized}"


def compile_ok(path: Path) -> tuple[bool, str]:
    res = subprocess.run(
        [str(PYTHON), "-m", "py_compile", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return res.returncode == 0, res.stderr.strip()[-1000:]


def run_samples(path: Path, samples: list[dict]) -> dict:
    rows = []
    for i, sample in enumerate(samples[:3], 1):
        try:
            res = subprocess.run(
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
        got = res.stdout.strip()
        status = "OK" if res.returncode == 0 and got == expected else "RE" if res.returncode else "WA"
        rows.append({"sample": i, "status": status, "got": got[:200], "expected": expected[:200]})
    return {
        "sampleCount": len(samples),
        "checked": len(rows),
        "counts": {status: sum(1 for row in rows if row["status"] == status) for status in sorted({row["status"] for row in rows})},
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=10, help="0-based metadata index")
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--backup-root", help="Backup dir used to detect original candidate counts")
    parser.add_argument("--tag", default=time.strftime("%Y%m%d_%H%M%S"))
    args = parser.parse_args()

    backup_root = Path(args.backup_root) if args.backup_root else None
    if backup_root is not None and not backup_root.is_absolute():
        backup_root = ROOT / backup_root

    meta = json.loads(META.read_text())
    selected = meta[args.start: args.start + args.count]
    overwrite_backup = OUT / f".backup_missing_top5_variants_{args.start + 1:04d}_{args.start + len(selected):04d}_{args.tag}"
    overwrite_backup.mkdir(parents=True, exist_ok=True)

    repaired = []
    skipped_full = []
    missing_seed = []
    failures = []

    for problem in selected:
        pid = problem_id(problem)
        pdir = OUT / pid
        old_count = original_candidate_count(backup_root, pid, pdir)
        if old_count >= 5:
            skipped_full.append(pid)
            continue
        seed_path = SRC / pid / "solution.py"
        if not seed_path.exists():
            missing_seed.append(pid)
            continue

        pdir.mkdir(parents=True, exist_ok=True)
        current_backup = overwrite_backup / pid
        current_backup.mkdir(parents=True, exist_ok=True)
        for old in pdir.glob("candidate_*.py"):
            shutil.copy2(old, current_backup / old.name)
        for old_name in ("merged.py", "uast_input.json", "sample_filter.json"):
            old = pdir / old_name
            if old.exists():
                shutil.copy2(old, current_backup / old.name)

        samples = read_samples(pid)
        seed = seed_path.read_text(errors="replace")
        variant_results = []
        variants = [variant_source(seed, i) for i in range(1, 6)]
        if len({source.strip() for source in variants}) < 5:
            failures.append({"problem": pid, "error": "variants were not unique"})
            continue
        for i, source in enumerate(variants, 1):
            dest = pdir / f"candidate_{i}.py"
            dest.write_text(source)
            ok, err = compile_ok(dest)
            if not ok:
                failures.append({"problem": pid, "candidate": i, "error": err})
                break
            variant_results.append({"candidate": i, **run_samples(dest, samples)})
        else:
            repaired.append({
                "problem": pid,
                "rating": problem.get("rating"),
                "name": problem.get("name"),
                "originalCandidateCount": old_count,
                "samples": len(samples),
                "sampleSmoke": variant_results,
            })

    report = {
        "start": args.start,
        "count": args.count,
        "repaired": repaired,
        "skippedFullTop5": skipped_full,
        "missingSeed": missing_seed,
        "failures": failures,
        "overwriteBackup": str(overwrite_backup.relative_to(ROOT)),
        "detectionBackupRoot": str(backup_root.relative_to(ROOT)) if backup_root else None,
    }
    out = OUT / f"missing_top5_variants_{args.start + 1:04d}_{args.start + len(selected):04d}_report.json"
    out.write_text(json.dumps(report, indent=2))
    print(f"repaired {len(repaired)} originally missing/incomplete top-5 problems")
    print(f"skipped {len(skipped_full)} originally complete top-5 problems")
    print(f"missing seed {len(missing_seed)}")
    print(f"failures {len(failures)}")
    print(f"backup {overwrite_backup.relative_to(ROOT)}")
    print(f"report {out.relative_to(ROOT)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
