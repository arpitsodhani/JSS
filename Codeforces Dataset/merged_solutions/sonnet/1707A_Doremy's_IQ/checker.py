"""1707A accepts any schedule that tests the maximum number of contests.

The printed string is replayed against Doremy's IQ rule, and its number of
tested contests has to match the reference answer's.
"""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        n = int(data[pos])
        q = int(data[pos + 1])
        pos += 2
        cases.append((q, [int(v) for v in data[pos:pos + n]]))
        pos += n
    wanted = [line.strip() for line in expected.split("\n") if line.strip()]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            q, a = cases[case]
            row = rows[case]
            assert len(row) == len(a), f"case {case + 1}: expected {len(a)} characters"
            iq = q
            for i, ch in enumerate(row):
                if ch == "0":
                    continue
                assert iq > 0, f"case {case + 1}: contest {i + 1} tested with no IQ left"
                if a[i] > iq:
                    iq -= 1
            assert row.count("1") == wanted[case].count("1"), \
                f"case {case + 1}: tested {row.count('1')} contests, best is {wanted[case].count('1')}"

    return check
