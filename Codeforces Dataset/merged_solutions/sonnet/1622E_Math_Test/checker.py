"""1622E accepts any permutation reaching the maximum surprise value.

The printed permutation is scored the same way as the reference one, and the
two totals have to agree.
"""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        pos += 2
        wanted = [int(v) for v in data[pos:pos + n]]
        pos += n
        sheets = data[pos:pos + n]
        pos += n
        cases.append((n, m, wanted, sheets))
    reference = [line.split() for line in expected.strip().split("\n")]

    def surprise(case, p):
        n, m, wanted, sheets = case
        total = 0
        for i in range(n):
            got = 0
            for j in range(m):
                if sheets[i][j] == "1":
                    got += p[j]
            total += abs(wanted[i] - got)
        return total

    def check(out):
        rows = [line.split() for line in out.strip().split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            n, m, wanted, sheets = cases[case]
            p = [int(v) for v in rows[case]]
            assert sorted(p) == list(range(1, m + 1)), f"case {case + 1}: not a permutation of 1..{m}"
            best = surprise(cases[case], [int(v) for v in reference[case]])
            here = surprise(cases[case], p)
            assert here == best, f"case {case + 1}: surprise {here}, best is {best}"

    return check
