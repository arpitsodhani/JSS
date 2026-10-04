"""1691B takes any valid shuffling, so the printed permutation is checked itself.

Every student must get someone else's shoes and those shoes must not be smaller
than their own size; -1 is right exactly when the reference says so.
"""


def check_for(stdin, expected):
    lines = stdin.split("\n")
    t = int(lines[0])
    cases = []
    pos = 1
    for _ in range(t):
        n = int(lines[pos])
        cases.append([int(v) for v in lines[pos + 1].split()])
        pos += 2
    wanted = [line.strip() for line in expected.split("\n") if line.strip()]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            sizes = cases[case]
            impossible = wanted[case] == "-1"
            if impossible:
                assert rows[case] == "-1", f"case {case + 1}: printed a shuffling, none exists"
                continue
            assert rows[case] != "-1", f"case {case + 1}: a shuffling exists"
            p = [int(v) for v in rows[case].split()]
            n = len(sizes)
            assert sorted(p) == list(range(1, n + 1)), f"case {case + 1}: not a permutation"
            for i in range(n):
                assert p[i] != i + 1, f"case {case + 1}: student {i + 1} kept their shoes"
                assert sizes[p[i] - 1] >= sizes[i], f"case {case + 1}: student {i + 1} got smaller shoes"

    return check
