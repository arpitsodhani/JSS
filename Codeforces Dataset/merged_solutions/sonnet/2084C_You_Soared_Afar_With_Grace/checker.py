"""2084C accepts any sequence of at most n swaps that makes a and b reverses.

The printed swaps are replayed on the input arrays and the result is compared
against the required a_i = b_{n+1-i}.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
        cases.append((a, b))
    verdicts = []
    for line in expected.split("\n"):
        line = line.strip()
        if line == "-1":
            verdicts.append(False)
        elif line and " " not in line:
            verdicts.append(True)

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        at = 0
        for case in range(t):
            a, b = cases[case]
            n = len(a)
            head = rows[at]
            at += 1
            if not verdicts[case]:
                assert head == "-1", f"case {case + 1}: printed swaps where none work"
                continue
            assert head != "-1", f"case {case + 1}: a solution exists"
            count = int(head)
            assert 0 <= count <= n, f"case {case + 1}: {count} swaps, the limit is {n}"
            a = list(a)
            b = list(b)
            for _ in range(count):
                i, j = (int(v) for v in rows[at].split())
                at += 1
                assert 1 <= i <= n and 1 <= j <= n and i != j, f"case {case + 1}: bad swap"
                a[i - 1], a[j - 1] = a[j - 1], a[i - 1]
                b[i - 1], b[j - 1] = b[j - 1], b[i - 1]
            for i in range(n):
                assert a[i] == b[n - 1 - i], f"case {case + 1}: a[{i + 1}] != b[{n - i}]"

    return check
