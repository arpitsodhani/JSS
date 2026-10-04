"""1547C accepts any interleaving that keeps both action orders legal."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        k = data[pos]
        n = data[pos + 1]
        m = data[pos + 2]
        pos += 3
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + m]
        pos += m
        cases.append((k, a, b))
    verdicts = [line.strip() != "-1" for line in expected.split("\n") if line.strip()]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            k, a, b = cases[case]
            if not verdicts[case]:
                assert rows[case] == "-1", f"case {case + 1}: printed a sequence where none exists"
                continue
            assert rows[case] != "-1", f"case {case + 1}: a sequence exists"
            steps = [int(v) for v in rows[case].split()]
            assert len(steps) == len(a) + len(b), f"case {case + 1}: wrong length"
            i = 0
            j = 0
            lines = k
            for value in steps:
                if i < len(a) and a[i] == value and (value == 0 or value <= lines):
                    i += 1
                elif j < len(b) and b[j] == value and (value == 0 or value <= lines):
                    j += 1
                else:
                    raise AssertionError(f"case {case + 1}: action {value} is not legal here")
                if value == 0:
                    lines += 1
            assert i == len(a) and j == len(b), f"case {case + 1}: not all actions were used"

    return check
