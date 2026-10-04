"""1342B accepts any string of minimal period containing t as a subsequence."""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    cases = [data[1 + i] for i in range(t)]
    reference = [line.strip() for line in expected.split("\n") if line.strip()]

    def period(s):
        n = len(s)
        for k in range(1, n + 1):
            if all(s[i] == s[i + k] for i in range(n - k)):
                return k
        return n

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            want = cases[case]
            got = rows[case]
            assert set(got) <= set("01"), f"case {case + 1}: only 0 and 1 allowed"
            assert len(got) <= 2 * len(want), f"case {case + 1}: too long"
            at = 0
            for ch in want:
                at = got.index(ch, at) + 1
            assert period(got) <= period(reference[case]), f"case {case + 1}: period is not minimal"

    return check
