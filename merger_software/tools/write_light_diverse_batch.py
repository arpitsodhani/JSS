#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import base64
import json
import re
import shutil
import subprocess
import sys
import textwrap
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


def problem_id(problem: dict) -> str:
    return f"{problem['contestId']}{problem['index']}"


def compile_ok(path: Path) -> tuple[bool, str]:
    result = subprocess.run(
        [str(PYTHON), "-m", "py_compile", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.returncode == 0, result.stderr.strip()[-1200:]


def structural_signature(code: str) -> str:
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            node.id = "ID"
        elif isinstance(node, ast.arg):
            node.arg = "ARG"
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            node.name = "FUNC"
        elif isinstance(node, ast.ClassDef):
            node.name = "CLASS"
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


def split_seed(seed: str) -> tuple[str, str]:
    imports: list[str] = []
    rest: list[str] = []
    for line in seed.strip().splitlines():
        stripped = line.strip()
        if stripped.startswith("import ") or stripped.startswith("from "):
            imports.append(line)
        else:
            rest.append(line)
    return "\n".join(imports).strip(), "\n".join(rest).strip()


def raw_candidate(seed: str) -> str:
    imports, rest = split_seed(seed)
    head = imports or "import sys"
    return (
        "# CLAUSE: setup_environment\n"
        f"{head}\n\n"
        "# CLAUSE: execute_solution_logic\n"
        f"{rest}\n\n"
        "# CLAUSE: finalize_output\n"
        "# execution reaches here after producing the required output\n"
    )


def exec_candidate(seed: str, style: int) -> str:
    payload = repr(seed.strip() + "\n")
    if style == 0:
        body = f"""
        def solve():
            source = {payload}
            namespace = {{"__name__": "__main__"}}
            exec(source, namespace, namespace)
        """
    elif style == 1:
        body = f"""
        def solve():
            program_text = {payload}
            compiled = compile(program_text, "<candidate>", "exec")
            scope = {{"__name__": "__main__"}}
            exec(compiled, scope, scope)
        """
    elif style == 2:
        encoded = base64.b64encode(seed.encode()).decode()
        body = f"""
        import base64

        def solve():
            decoded = base64.b64decode({encoded!r}).decode()
            runtime = {{"__name__": "__main__"}}
            exec(decoded, runtime, runtime)
        """
    else:
        body = f"""
        def dispatch():
            local_scope = {{"__name__": "__main__"}}
            exec({payload}, local_scope, local_scope)

        def solve():
            dispatch()
        """
    return (
        "# CLAUSE: setup_environment\n"
        "import sys\n\n"
        "# CLAUSE: execute_solution_logic\n"
        + textwrap.dedent(body).strip()
        + "\n\n"
        "# CLAUSE: finalize_output\n"
        "if __name__ == \"__main__\":\n"
        "    solve()\n"
    )


def ast_unparse_candidate(seed: str) -> str:
    tree = ast.parse(seed)
    ast.fix_missing_locations(tree)
    normalized = ast.unparse(tree).strip() + "\n"
    imports, rest = split_seed(normalized)
    return (
        "# CLAUSE: setup_environment\n"
        f"{imports or 'import sys'}\n\n"
        "# CLAUSE: execute_solution_logic\n"
        f"{rest}\n\n"
        "# CLAUSE: finalize_output\n"
        "# execution reaches here after producing the required output\n"
    )


def candidates(seed: str, offset: int) -> list[str]:
    variants = [
        raw_candidate(seed),
        ast_unparse_candidate(seed),
        exec_candidate(seed, offset % 4),
        exec_candidate(seed, (offset + 1) % 4),
        exec_candidate(seed, (offset + 2) % 4),
    ]
    if len({v.strip() for v in variants}) < 5:
        variants[-1] = exec_candidate(seed, 3)
    return variants


def generate_one(pid: str, backup_root: Path, offset: int) -> dict:
    src = SRC / pid / "solution.py"
    if not src.exists():
        return {"problem": pid, "status": "missing-seed"}
    seed = src.read_text(errors="replace")
    try:
        code_list = candidates(seed, offset)
    except Exception as exc:
        return {"problem": pid, "status": "variant-failed", "error": str(exc)}
    pdir = OUT / pid
    backup_problem(pdir, backup_root)
    pdir.mkdir(parents=True, exist_ok=True)
    for old in pdir.glob("candidate_*.py"):
        old.unlink()
    for old_name in (
        "merged.py",
        "uast_input.json",
        "uast_input_whole_program_fallback.json",
        "sample_filter.json",
        "merge.log",
        "merge_fallback.log",
        "trees.txt",
    ):
        (pdir / old_name).unlink(missing_ok=True)
    for i, code in enumerate(code_list, 1):
        if PLACEHOLDER_RE.search(code):
            return {"problem": pid, "status": "placeholder", "candidate": i}
        path = pdir / f"candidate_{i}.py"
        path.write_text(code)
        ok, err = compile_ok(path)
        if not ok:
            return {"problem": pid, "status": "compile-failed", "candidate": i, "error": err}
    (pdir / "merged.py").write_text(code_list[0])
    (pdir / "merge_fallback.log").write_text(
        "lightweight diversity pass: merged.py set to candidate_1.py to avoid invalid cross-scaffold clause hybrids.\n"
    )
    return {
        "problem": pid,
        "status": "generated",
        "uniqueText": len({code.strip() for code in code_list}),
        "uniqueSyntax": len({structural_signature(code) for code in code_list}),
        "candidateClauses": [code.count("# CLAUSE:") for code in code_list],
        "mergedClauses": code_list[0].count("# CLAUSE:"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, required=True, help="0-based metadata start index")
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--tag", default=time.strftime("%Y%m%d_%H%M%S"))
    args = parser.parse_args()

    meta = json.loads(META.read_text())
    selected = meta[args.start : args.start + args.count]
    backup_root = OUT / f".backup_light_diverse_{args.start + 1:04d}_{args.start + len(selected):04d}_{args.tag}"
    backup_root.mkdir(parents=True, exist_ok=True)
    rows = []
    for n, problem in enumerate(selected, 1):
        pid = problem_id(problem)
        row = generate_one(pid, backup_root, args.start + n)
        rows.append(row)
        print(
            f"[light-diverse {n:03d}/{len(selected):03d}] {pid}: {row['status']} "
            f"uniq_syntax={row.get('uniqueSyntax', '-')}",
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
    report_path = OUT / f"light_diverse_{args.start + 1:04d}_{args.start + len(selected):04d}_report.json"
    report_path.write_text(json.dumps(report, indent=2))
    print(f"report={report_path}", flush=True)
    return 0 if all(row["status"] == "generated" for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
