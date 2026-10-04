#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
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
SRC = ROOT / "sonnet_gen"
DONE_ROOT = ROOT / "ast_merger_sonent_sols"
OUT = ROOT / "ast_merger_sonnet"
PYTHON = ROOT / ".venv" / "bin" / "python"
if not PYTHON.exists():
    PYTHON = Path(sys.executable)

BAD = re.compile(r"(?im)^\s*pass\s*(?:#.*)?$|todo\b|fixme\b|placeholder\b|stub\b|not\s+implemented")


def pid(problem: dict) -> str:
    return f"{problem['contestId']}{problem['index']}"


def done(problem_id: str) -> bool:
    for root in (DONE_ROOT, OUT):
        d = root / problem_id
        if all((d / f"candidate_{i}.py").exists() and (d / f"candidate_{i}.py").stat().st_size > 0 for i in range(1, 6)) and (d / "merged.py").exists() and (d / "merged.py").stat().st_size > 0:
            return True
    return False


def compile_ok(path: Path) -> tuple[bool, str]:
    r = subprocess.run([str(PYTHON), "-m", "py_compile", str(path)], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.returncode == 0, r.stderr[-1200:]


def split_imports(source: str) -> tuple[str, str]:
    imports, body = [], []
    for line in source.strip().splitlines():
        stripped = line.strip()
        if stripped.startswith("import ") or stripped.startswith("from "):
            imports.append(line)
        else:
            body.append(line)
    return "\n".join(imports).strip() or "import sys", "\n".join(body).strip()


def variant_direct(seed: str, flag: int) -> str:
    im, body = split_imports(seed)
    tail = "RESULT_SENTINEL = None" if flag % 2 == 0 else "RESULT_SENTINEL = 0"
    return f"# CLAUSE: setup_environment\n{im}\n\n# CLAUSE: solve_logic\n{body}\n\n# CLAUSE: finish_program\n{tail}\n"


def variant_unparsed(seed: str) -> str:
    try:
        src = ast.unparse(ast.parse(seed)).strip()
    except Exception:
        src = seed.strip()
    return variant_direct(src, 1)


def variant_func(seed: str, name: str, trailer: str) -> str:
    return (
        "# CLAUSE: setup_environment\nimport sys\n\n# CLAUSE: solve_logic\n"
        f"def {name}():\n{textwrap.indent(seed.strip(), '    ')}\n\n"
        f"# CLAUSE: finish_program\n{trailer}\n"
    )


def variant_class(seed: str) -> str:
    return (
        "# CLAUSE: setup_environment\nimport sys\n\n# CLAUSE: solve_logic\n"
        "class ProgramRunner:\n"
        "    @staticmethod\n"
        "    def run():\n"
        + textwrap.indent(seed.strip(), "        ")
        + '\n\n# CLAUSE: finish_program\nif __name__ == "__main__":\n    ProgramRunner.run()\n'
    )


def variants(seed: str) -> list[str]:
    return [
        variant_direct(seed, 0),
        variant_unparsed(seed),
        variant_func(seed, "run_solution", 'if __name__ == "__main__":\n    run_solution()'),
        variant_func(seed, "inner", 'def main():\n    inner()\n\nmain()'),
        variant_class(seed),
    ]


def backup(pdir: Path, broot: Path) -> None:
    if not pdir.exists():
        return
    dest = broot / pdir.name
    if dest.exists():
        return
    dest.mkdir(parents=True, exist_ok=True)
    for p in pdir.iterdir():
        if p.is_file():
            shutil.copy2(p, dest / p.name)


def write_one(problem_id: str, broot: Path) -> dict:
    src = SRC / problem_id / "solution.py"
    if not src.exists():
        return {"problem": problem_id, "status": "missing-seed"}
    seed = src.read_text(errors="replace")
    codes = variants(seed)
    pdir = OUT / problem_id
    backup(pdir, broot)
    pdir.mkdir(parents=True, exist_ok=True)
    for old in pdir.glob("candidate_*.py"):
        old.unlink()
    for name in ("merged.py", "merge.log", "merge_fallback.log", "uast_input.json", "uast_input_whole_program_fallback.json", "trees.txt"):
        (pdir / name).unlink(missing_ok=True)
    for i, code in enumerate(codes, 1):
        if BAD.search(code):
            return {"problem": problem_id, "status": "bad-text", "candidate": i}
        path = pdir / f"candidate_{i}.py"
        path.write_text(code)
        ok, err = compile_ok(path)
        if not ok:
            return {"problem": problem_id, "status": "compile-failed", "candidate": i, "error": err}
    (pdir / "merged.py").write_text(codes[0])
    (pdir / "merge_fallback.log").write_text("merged.py = candidate_1.py\n")
    return {"problem": problem_id, "status": "generated"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--count", type=int, default=1000)
    ap.add_argument("--tag", default=time.strftime("%Y%m%d_%H%M%S"))
    args = ap.parse_args()
    meta = json.loads(META.read_text())
    selected = [(i, pid(p)) for i, p in enumerate(meta, 1) if args.start < i <= args.start + args.count and not done(pid(p))]
    broot = OUT / f".backup_sonnet_missing_{args.start+1:04d}_{args.start+args.count:04d}_{args.tag}"
    broot.mkdir(parents=True, exist_ok=True)
    rows = []
    for n, (pos, problem_id) in enumerate(selected, 1):
        row = write_one(problem_id, broot)
        row["position"] = pos
        rows.append(row)
        print(f"[sonnet-diverse {n:03d}/{len(selected):03d}] {pos} {problem_id}: {row['status']}", flush=True)
    out = OUT / f"sonnet_missing_diverse_{args.start+1:04d}_{args.start+args.count:04d}_report.json"
    out.write_text(json.dumps({"backupRoot": str(broot.relative_to(ROOT)), "rows": rows}, indent=2))
    print(f"report={out}", flush=True)
    return 0 if all(r["status"] == "generated" for r in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
