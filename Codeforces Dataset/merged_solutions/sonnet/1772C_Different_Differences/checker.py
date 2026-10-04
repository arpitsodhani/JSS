"""1772C accepts any increasing array with the largest characteristic."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    cases = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(t)]
    reference = [line.split() for line in expected.split("\n") if line.strip()]

    def characteristic(row):
        return len({row[i + 1] - row[i] for i in range(len(row) - 1)})

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            k, n = cases[case]
            row = [int(v) for v in rows[case]]
            assert len(row) == k, f"case {case + 1}: expected {k} values"
            assert all(1 <= v <= n for v in row), f"case {case + 1}: a value is outside 1..{n}"
            assert all(row[i] < row[i + 1] for i in range(k - 1)), f"case {case + 1}: not increasing"
            best = characteristic([int(v) for v in reference[case]])
            here = characteristic(row)
            assert here >= best, f"case {case + 1}: characteristic {here}, best is {best}"

    return check
