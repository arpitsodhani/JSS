#!/usr/bin/env python3
"""Validate ast_merger_sonent_sols candidates: compile, structural homogeneity, samples."""
from __future__ import annotations

import ast
import itertools
import json
import subprocess
import sys
import threading
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sonnet_clauses import split_clauses, split_clauses_full

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ast_merger_sonent_sols"
PYTHON = ROOT / ".venv" / "bin" / "python"
if not PYTHON.exists():
    PYTHON = Path(sys.executable)


def run(path: Path, stdin: str, timeout: int = 20) -> str:
    res = subprocess.run(
        [str(PYTHON), str(path)],
        input=stdin,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )
    if res.returncode != 0:
        raise AssertionError(f"crashed rc={res.returncode}\n{res.stderr[-800:]}")
    return res.stdout


def norm(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def exact(expected: str):
    def check(out: str) -> None:
        if norm(out) != norm(expected):
            raise AssertionError(f"expected {norm(expected)!r}, got {norm(out)!r}")
    return check


# ---------------------------------------------------------------- checkers

def check_2084A(out: str) -> None:
    lines = norm(out).splitlines()
    ns = [2, 3, 4, 5]
    assert len(lines) == len(ns), f"line count {len(lines)}"
    for n, line in zip(ns, lines):
        if n % 2 == 0:
            assert line.strip() == "-1", f"n={n}: {line!r}"
            continue
        p = list(map(int, line.split()))
        assert sorted(p) == list(range(1, n + 1)), f"n={n} not a permutation: {line!r}"
        for i in range(2, n + 1):
            assert max(p[i - 2], p[i - 1]) % i == i - 1, f"n={n} fails at i={i}: {line!r}"


def check_1715B(out: str) -> None:
    cases = [
        (1, 6, 3, 100), (3, 6, 3, 12), (3, 6, 3, 19), (5, 4, 7, 38),
        (5, 4, 7, 80), (99978, 10 ** 9, 10 ** 8, 10 ** 18), (1, 1, 0, 0),
        (4, 10 ** 9, 10 ** 9, 10 ** 18),
    ]
    lines = norm(out).splitlines()
    assert len(lines) == len(cases), f"line count {len(lines)}"
    for (n, k, b, s), line in zip(cases, lines):
        feasible = k * b <= s <= k * b + n * (k - 1)
        if not feasible:
            assert line.strip() == "-1", f"{n} {k} {b} {s}: expected -1, got {line!r}"
            continue
        arr = list(map(int, line.split()))
        assert len(arr) == n, f"{n} {k} {b} {s}: length {len(arr)}"
        assert all(v >= 0 for v in arr), f"{n} {k} {b} {s}: negative value"
        assert sum(arr) == s, f"{n} {k} {b} {s}: sum {sum(arr)}"
        assert sum(v // k for v in arr) == b, f"{n} {k} {b} {s}: beauty wrong"


def make_check_801B(x: str, y: str):
    def check(out: str) -> None:
        z = norm(out)
        if any(yc > xc for xc, yc in zip(x, y)):
            assert z == "-1", f"expected -1, got {z!r}"
            return
        assert len(z) == len(x), f"length {len(z)}"
        assert z.isalpha() and z.islower(), f"bad alphabet {z!r}"
        got = "".join(min(a, b) for a, b in zip(x, z))
        assert got == y, f"f(x,z)={got!r} != {y!r}"
    return check


SAMPLES = {
    "1693B": [
        ("4\n2\n1\n1 5\n2 9\n3\n1 1\n4 5\n2 4\n6 10\n4\n1 2 1\n6 9\n5 6\n4 5\n2 4\n5\n1 2 3 4\n5 5\n4 4\n3 3\n2 2\n1 1\n",
         exact("1\n2\n2\n5")),
    ],
    "2084A": [("4\n2\n3\n4\n5\n", check_2084A)],
    "180D": [
        ("aad\naac\n", exact("aad")),
        ("abad\nbob\n", exact("daab")),
        ("abc\ndefg\n", exact("-1")),
        ("czaaab\nabcdef\n", exact("abczaa")),
    ],
    "985C": [
        ("4 2 1\n2 2 1 2 3 2 2 3\n", exact("7")),
        ("2 1 0\n10 10\n", exact("20")),
        ("1 2 1\n5 2\n", exact("2")),
        ("3 2 1\n1 2 3 4 5 6\n", exact("0")),
    ],
    "519C": [("2 6\n", exact("2")), ("4 5\n", exact("3"))],
    "1715B": [
        ("8\n1 6 3 100\n3 6 3 12\n3 6 3 19\n5 4 7 38\n5 4 7 80\n"
         "99978 1000000000 100000000 1000000000000000000\n1 1 0 0\n"
         "4 1000000000 1000000000 1000000000000000000\n", check_1715B),
    ],
    "2051F": [
        ("5\n6 5 3\n1 2 3\n2 1 4\n2 1 1 2\n5 3 1\n3\n3 2 4\n2 1 1 1\n18 15 4\n13 15 1 16\n",
         exact("2 3 5\n2 2 2 2\n2\n2 3 3 3\n2 4 6 8")),
    ],
    "534B": [("5 6\n4 2\n", exact("26")), ("10 10\n10 0\n", exact("100"))],
    "801B": [
        ("ab\naa\n", make_check_801B("ab", "aa")),
        ("nzwzl\nniwel\n", make_check_801B("nzwzl", "niwel")),
        ("ab\nba\n", make_check_801B("ab", "ba")),
    ],
    "500A": [
        ("8 4\n1 2 1 2 1 2 1\n", exact("YES")),
        ("8 5\n1 2 1 2 1 1 1\n", exact("NO")),
        ("1 1\n\n", exact("YES")),
        ("2 2\n1\n", exact("YES")),
    ],
    "2210B": [
        ("4\n3\n3 2 1\n5\n4 3 2 5 1\n4\n4 2 1 3\n4\n2 3 4 1\n", exact("2\n2\n3\n1")),
    ],
    "2062C": [
        ("5\n1\n-1000\n2\n5 -3\n2\n1000 1\n9\n9 7 9 -9 9 -8 7 -8 9\n"
         "11\n678 201 340 444 453 922 128 987 127 752 0\n",
         exact("-1000\n8\n1001\n2056\n269891")),
    ],
    "2070B": [
        ("6\n3 2 6\nLLR\n2 -1 8\nRL\n4 -2 5\nLRRR\n5 3 7\nLRRLL\n1 1 1\nL\n"
         "3 -1 4846549234412827\nRLR\n",
         exact("1\n4\n1\n0\n1\n2423274617206414")),
    ],
    "203B": [
        ("4 11\n1 1\n1 2\n1 3\n2 2\n2 3\n1 4\n2 4\n3 4\n3 2\n3 3\n4 1\n", exact("10")),
        ("4 12\n1 1\n1 2\n1 3\n2 2\n2 3\n1 4\n2 4\n3 4\n3 2\n4 2\n4 1\n3 1\n", exact("-1")),
    ],
    "1223D": [
        ("3\n7\n3 1 6 6 3 1 1\n8\n1 1 4 4 4 7 8 8\n7\n4 2 5 2 6 2 7\n", exact("2\n0\n1")),
    ],
}


def style_signature(code: str) -> tuple[int, int, int]:
    tree = ast.parse(code)
    funcs = sum(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) for n in ast.walk(tree))
    classes = sum(isinstance(n, ast.ClassDef) for n in ast.walk(tree))
    imports = sum(isinstance(n, (ast.Import, ast.ImportFrom)) for n in tree.body)
    return funcs, classes, imports


def top_level_defs(code: str) -> list[str]:
    tree = ast.parse(code)
    return [n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]


def assemble(includes, chosen_clauses) -> str:
    """Reproduce the composer's assembly for an arbitrary clause combination."""
    parts = ["\n".join(includes), ""]
    for cid, code in chosen_clauses:
        parts.append(code)
        parts.append("")
    return "\n".join(parts) + "\n"


def run_source(source: str, stdin: str) -> str:
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as fh:
        fh.write(source)
        tmp = Path(fh.name)
    try:
        return run(tmp, stdin)
    finally:
        tmp.unlink(missing_ok=True)


def load_interactor(pid: str):
    """An interactive problem ships interactor.py instead of fixed sample I/O.

    It exposes tests() -> list of cases and interact(case, send, readline), which
    plays the judge's side and raises AssertionError on any protocol violation,
    query-budget overrun, or wrong final answer. Statement samples for these
    problems are transcripts of one particular interaction, so they cannot be fed
    to a program as stdin.
    """
    path = OUT / pid / "interactor.py"
    if not path.exists():
        return None
    namespace: dict = {}
    exec(compile(path.read_text(), str(path), "exec"), namespace)  # noqa: S102
    return namespace


def run_interactive(path: Path, interactor, timeout: int = 30) -> None:
    for case in interactor["tests"]():
        proc = subprocess.Popen(
            [str(PYTHON), str(path)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, bufsize=1,
        )
        killer = threading.Timer(timeout, proc.kill)
        killer.start()

        def send(line: str) -> None:
            proc.stdin.write(line + "\n")
            proc.stdin.flush()

        def readline() -> str:
            line = proc.stdout.readline()
            if not line:
                raise AssertionError(f"program stopped responding: {proc.stderr.read()[-400:]}")
            return line.strip()

        try:
            interactor["interact"](case, send, readline)
        finally:
            killer.cancel()
            proc.kill()
            proc.wait()


def run_source_interactive(source: str, interactor) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as fh:
        fh.write(source)
        tmp = Path(fh.name)
    try:
        run_interactive(tmp, interactor)
    finally:
        tmp.unlink(missing_ok=True)


def samples_for(pid: str) -> list:
    """Sample cases for a problem.

    The 15 hand-tuned problems keep their curated SAMPLES entries. Everything
    generated later is checked against problem.json, which holds the statement's
    own sample I/O fetched verbatim from Codeforces (the copy in
    codeforces_data/statements has had its newlines stripped, so it cannot be
    fed to a program). A problem whose answer is not unique ships a checker.py
    next to its candidates exposing check_for(stdin, expected) -> check(out).
    """
    if pid in SAMPLES:
        return SAMPLES[pid]
    pdir = OUT / pid
    if (pdir / "interactor.py").exists():
        return []
    prob = pdir / "problem.json"
    if not prob.exists():
        return []
    data = json.loads(prob.read_text())
    if data.get("error"):
        return []
    checker = pdir / "checker.py"
    make = None
    if checker.exists():
        namespace: dict = {}
        exec(compile(checker.read_text(), str(checker), "exec"), namespace)  # noqa: S102
        make = namespace["check_for"]
    cases = []
    for sample in data.get("samples", []):
        stdin, expected = sample["input"], sample["output"]
        cases.append((stdin, make(stdin, expected) if make else exact(expected)))
    return cases


def check_problem(pid: str, combos: int = 0) -> list[str]:
    problems = []
    pdir = OUT / pid
    paths = [pdir / f"candidate_{i}.py" for i in range(1, 6)]
    missing = [p.name for p in paths if not p.exists()]
    if missing:
        return [f"{pid}: missing {', '.join(missing)}"]

    sources = [p.read_text() for p in paths]
    sigs, defs = [], []
    for path, src in zip(paths, sources):
        try:
            sigs.append(style_signature(src))
            defs.append(tuple(top_level_defs(src)))
        except SyntaxError as exc:
            problems.append(f"{pid}/{path.name}: syntax error {exc}")
    if len(set(sigs)) > 1:
        problems.append(f"{pid}: style signatures differ {sigs}")
    if len(set(defs)) > 1:
        problems.append(f"{pid}: top-level defs differ {defs}")
    if len({s.strip() for s in sources}) != 5:
        problems.append(f"{pid}: duplicate candidate bodies")

    split = [split_clauses(path) for path in paths]
    ids = [tuple(cid for cid, _ in clauses) for _, clauses in split]
    if len(set(ids)) > 1:
        problems.append(f"{pid}: clause decompositions differ {ids}")
    if len({tuple(inc) for inc, _ in split}) > 1:
        problems.append(f"{pid}: include blocks differ")
    for path, (_, clauses) in zip(paths, split):
        for cid, code in clauses:
            if not code.strip():
                problems.append(f"{pid}/{path.name}: clause {cid} is empty")

    sigs = [tuple(split_clauses_full(path)[1]) for path in paths]
    declared = [tuple((cid, sig) for cid, sig, _ in s) for s in sigs]
    if len(set(declared)) > 1:
        problems.append(f"{pid}: declared clause signatures differ across candidates")
    if any(not sig for cid, sig in declared[0]):
        problems.append(f"{pid}: some clauses declare no signature")

    interactor = load_interactor(pid)
    if interactor is not None:
        for path in paths:
            try:
                run_interactive(path, interactor)
            except AssertionError as exc:
                problems.append(f"{pid}/{path.name}: {exc}")

    for path in paths:
        for stdin, check in samples_for(pid):
            try:
                check(run(path, stdin))
            except subprocess.TimeoutExpired:
                problems.append(f"{pid}/{path.name}: timeout on {stdin[:30]!r}")
            except AssertionError as exc:
                problems.append(f"{pid}/{path.name}: {exc}")

    merged = pdir / "merged.py"
    if merged.exists() and interactor is not None:
        try:
            run_interactive(merged, interactor)
        except AssertionError as exc:
            problems.append(f"{pid}/merged.py: {exc}")
    if merged.exists():
        for stdin, check in samples_for(pid):
            try:
                check(run(merged, stdin))
            except AssertionError as exc:
                problems.append(f"{pid}/merged.py: {exc}")

    if combos and len(set(ids)) == 1 and not problems:
        n_clauses = len(ids[0])
        picks = list(itertools.product(range(5), repeat=n_clauses))
        if len(picks) > combos:
            step = len(picks) / combos
            picks = [picks[int(i * step)] for i in range(combos)]
        includes = split[0][0]
        for pick in picks:
            source = assemble(includes, [split[p][1][c] for c, p in enumerate(pick)])
            label = "+".join(f"c{c + 1}:P{p + 1}" for c, p in enumerate(pick))
            if interactor is not None:
                try:
                    run_source_interactive(source, interactor)
                except AssertionError as exc:
                    problems.append(f"{pid} combo {label}: {exc}")
                    break
            for stdin, check in samples_for(pid):
                try:
                    check(run_source(source, stdin))
                except Exception as exc:
                    problems.append(f"{pid} combo {label}: {exc}")
                    break
    return problems


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    combos = 0
    for a in sys.argv[1:]:
        if a.startswith("--combos="):
            combos = int(a.split("=", 1)[1])
    # A directory holding only problem.json is a fetched-but-not-yet-written
    # problem: report it as pending rather than as a failure, so a part-finished
    # batch still verifies cleanly.
    all_dirs = sorted(p for p in OUT.iterdir() if p.is_dir() and p.name != "codeforces_data")
    pending = [p.name for p in all_dirs if not (p / "candidate_1.py").exists()]
    pids = args or [p.name for p in all_dirs if (p / "candidate_1.py").exists()]
    failures = []
    for pid in pids:
        issues = check_problem(pid, combos=combos)
        if issues:
            failures.extend(issues)
            print(f"FAIL {pid}")
            for line in issues:
                print(f"   {line}")
        else:
            sig = style_signature((OUT / pid / "candidate_1.py").read_text())
            cids = [cid for cid, _ in split_clauses(OUT / pid / "candidate_1.py")[1]]
            print(f"ok   {pid:6s} signature{sig}  clauses={cids}")
    print()
    if pending and not args:
        print(f"pending (statement fetched, candidates not written yet): {' '.join(pending)}")
    print(f"{len(pids) - len({f.split(':')[0].split('/')[0] for f in failures})}/{len(pids)} problems clean")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
