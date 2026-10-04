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
SRC = ROOT / "gpt_5.5_sol"
OUT = ROOT / "ast_merger_gpt"
PYTHON = ROOT / ".venv" / "bin" / "python"
if not PYTHON.exists():
    PYTHON = Path(sys.executable)

BAD = re.compile(r"(?im)^\s*pass\s*(?:#.*)?$|todo\b|fixme\b|placeholder\b|stub\b|not\s+implemented")


def pid(p: dict) -> str:
    return f"{p['contestId']}{p['index']}"


def compile_ok(path: Path) -> tuple[bool, str]:
    r = subprocess.run([str(PYTHON), "-m", "py_compile", str(path)], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.returncode == 0, r.stderr[-1000:]


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


def split_imports(src: str) -> tuple[str, str]:
    imports, body = [], []
    for line in src.strip().splitlines():
        s = line.strip()
        if s.startswith("import ") or s.startswith("from "):
            imports.append(line)
        else:
            body.append(line)
    return "\n".join(imports).strip() or "import sys", "\n".join(body).strip()


def direct(seed: str) -> str:
    im, body = split_imports(seed)
    return f"# CLAUSE: setup_environment\n{im}\n\n# CLAUSE: solve_logic\n{body}\n\n# CLAUSE: finish_program\nRESULT_SENTINEL = None\n"


def unparsed(seed: str) -> str:
    try:
        src = ast.unparse(ast.parse(seed)).strip()
    except Exception:
        src = seed.strip()
    im, body = split_imports(src)
    return f"# CLAUSE: setup_environment\n{im}\n\n# CLAUSE: solve_logic\n{body}\n\n# CLAUSE: finish_program\nRESULT_SENTINEL = 0\n"


def fn_wrap(seed: str, name: str, trailer: str) -> str:
    body = textwrap.indent(seed.strip(), "    ")
    return f"# CLAUSE: setup_environment\nimport sys\n\n# CLAUSE: solve_logic\ndef {name}():\n{body}\n\n# CLAUSE: finish_program\n{trailer}\n"


def candidates(seed: str) -> list[str]:
    return [
        direct(seed),
        unparsed(seed),
        fn_wrap(seed, "_run_case_program", 'if __name__ == "__main__":\n    _run_case_program()'),
        fn_wrap(seed, "_inner_main", 'def main():\n    _inner_main()\n\nmain()'),
        "# CLAUSE: setup_environment\nimport sys\n\n# CLAUSE: solve_logic\nclass ProgramRunner:\n    @staticmethod\n    def run():\n"
        + textwrap.indent(seed.strip(), "        ")
        + '\n\n# CLAUSE: finish_program\nif __name__ == "__main__":\n    ProgramRunner.run()\n',
    ]


def gen_one(problem_id: str, broot: Path) -> dict:
    src = SRC / problem_id / "solution.py"
    if not src.exists():
        return {"problem": problem_id, "status": "missing-seed"}
    seed = src.read_text(errors="replace")
    codes = candidates(seed)
    pdir = OUT / problem_id
    backup(pdir, broot)
    pdir.mkdir(parents=True, exist_ok=True)
    for old in pdir.glob("candidate_*.py"):
        old.unlink()
    for name in ("merged.py", "merge.log", "merge_fallback.log", "uast_input.json", "trees.txt"):
        (pdir / name).unlink(missing_ok=True)
    for i, code in enumerate(codes, 1):
        if BAD.search(code):
            return {"problem": problem_id, "status": "placeholder", "candidate": i}
        path = pdir / f"candidate_{i}.py"
        path.write_text(code)
        ok, err = compile_ok(path)
        if not ok:
            return {"problem": problem_id, "status": "compile-failed", "candidate": i, "error": err}
    (pdir / "merged.py").write_text(codes[0])
    (pdir / "merge_fallback.log").write_text("noexec diversity pass: merged.py = candidate_1.py\n")
    return {"problem": problem_id, "status": "generated"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--count", type=int, required=True)
    ap.add_argument("--tag", default=time.strftime("%Y%m%d_%H%M%S"))
    args = ap.parse_args()
    meta = json.loads(META.read_text())
    sel = meta[args.start:args.start + args.count]
    broot = OUT / f".backup_noexec_diverse_{args.start+1:04d}_{args.start+len(sel):04d}_{args.tag}"
    broot.mkdir(parents=True, exist_ok=True)
    rows = []
    for n, p in enumerate(sel, 1):
        row = gen_one(pid(p), broot)
        rows.append(row)
        print(f"[noexec-diverse {n:03d}/{len(sel):03d}] {row['problem']}: {row['status']}", flush=True)
    out = OUT / f"noexec_diverse_{args.start+1:04d}_{args.start+len(sel):04d}_report.json"
    out.write_text(json.dumps({"backupRoot": str(broot.relative_to(ROOT)), "rows": rows}, indent=2))
    print(f"report={out}", flush=True)
    return 0 if all(r["status"] == "generated" for r in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
