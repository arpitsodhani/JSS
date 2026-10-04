#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST_FIVE = ["1693B", "2084A", "180D", "985C", "519C"]


def run_solution(problem_id: str, stdin: str) -> str:
    path = ROOT / "codeforces_sols" / problem_id / "solution.py"
    result = subprocess.run(
        [sys.executable, str(path)],
        input=stdin,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"{problem_id} crashed:\n{result.stderr}")
    return result.stdout.strip()


def check_2084(output: str) -> None:
    ns = [2, 3, 4, 5]
    lines = output.splitlines()
    assert len(lines) == len(ns), output
    for n, line in zip(ns, lines):
        if n % 2 == 0:
            assert line.strip() == "-1", output
            continue
        p = list(map(int, line.split()))
        assert sorted(p) == list(range(1, n + 1)), output
        for i in range(2, n + 1):
            assert max(p[i - 2], p[i - 1]) % i == i - 1, output


def main() -> int:
    checks = [
        (
            "1693B",
            "4\n2\n1\n1 5\n2 9\n3\n1 1\n4 5\n2 4\n6 10\n4\n1 2 1\n6 9\n5 6\n4 5\n2 4\n5\n1 2 3 4\n5 5\n4 4\n3 3\n2 2\n1 1\n",
            "1\n2\n2\n5",
        ),
        ("180D", "aad\naac\n", "aad"),
        ("180D", "abad\nbob\n", "daab"),
        ("180D", "abc\ndefg\n", "-1"),
        ("180D", "czaaab\nabcdef\n", "abczaa"),
        ("985C", "4 2 1\n2 2 1 2 3 2 2 3\n", "7"),
        ("985C", "2 1 0\n10 10\n", "20"),
        ("985C", "1 2 1\n5 2\n", "2"),
        ("985C", "3 2 1\n1 2 3 4 5 6\n", "0"),
        ("519C", "2 6\n", "2"),
        ("519C", "4 5\n", "3"),
    ]

    for problem_id, stdin, expected in checks:
        actual = run_solution(problem_id, stdin)
        assert actual == expected, f"{problem_id}: expected {expected!r}, got {actual!r}"

    check_2084(run_solution("2084A", "4\n2\n3\n4\n5\n"))
    print("Verified sample checks for " + ", ".join(FIRST_FIVE))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
