"""762C accepts any result of deleting one shortest run of characters from b so
that what is left is a subsequence of a.

The checker recomputes the best achievable length with its own prefix/suffix
scan and then verifies the printed string really is b minus one block.
"""


def check_for(stdin, expected):
    a, b = stdin.split()[:2]
    n, m = len(a), len(b)
    big = n + 1
    prefix = [0] * (m + 1)
    at = 0
    for i in range(m):
        if at < big:
            while at < n and a[at] != b[i]:
                at += 1
            at = big if at == n else at + 1
        prefix[i + 1] = at
    suffix = [0] * (m + 1)
    at = 0
    for j in range(m - 1, -1, -1):
        if at < big:
            while at < n and a[n - 1 - at] != b[j]:
                at += 1
            at = big if at == n else at + 1
        suffix[j] = at
    suffix[m] = 0
    best = None
    for i in range(m + 1):
        if prefix[i] > n:
            break
        for j in range(i, m + 1):
            if prefix[i] + suffix[j] <= n:
                if best is None or j - i < best:
                    best = j - i
                break
    target = m - best

    def is_subsequence(t, s):
        it = iter(s)
        return all(ch in it for ch in t)

    def check(out):
        text = out.strip()
        got = "" if text == "-" else text
        assert len(got) == target, f"printed length {len(got)}, the best is {target}"
        assert is_subsequence(got, a), "the answer is not a subsequence of a"
        ok = False
        for i in range(m + 1):
            for j in range(i, m + 1):
                if b[:i] + b[j:] == got:
                    ok = True
                    break
            if ok:
                break
        assert ok, "the answer is not b with one block removed"

    return check
