"""1681C accepts any sequence of at most 1e4 swaps that sorts both arrays."""


def check_for(stdin, expected):
    tokens = [int(v) for v in stdin.split()]
    cases = []
    pos = 1
    for _ in range(tokens[0]):
        n = tokens[pos]
        pos += 1
        a = tokens[pos:pos + n]
        pos += n
        b = tokens[pos:pos + n]
        pos += n
        cases.append((n, a, b))

    def sortable(n, a, b):
        order = sorted(range(n), key=lambda i: (a[i], b[i]))
        bb = [b[i] for i in order]
        return all(bb[i] <= bb[i + 1] for i in range(n - 1))

    def check(out):
        got = [int(v) for v in out.split()]
        at = 0
        for n, a, b in cases:
            head = got[at]
            at += 1
            if head == -1:
                assert not sortable(n, a, b), "printed -1 but both arrays can be sorted"
                continue
            assert sortable(n, a, b), "printed a plan but sorting is impossible"
            assert 0 <= head <= 10000, f"{head} moves is outside [0, 1e4]"
            x = list(a)
            y = list(b)
            for _ in range(head):
                i, j = got[at] - 1, got[at + 1] - 1
                at += 2
                assert 0 <= i < n and 0 <= j < n and i != j, "bad swap"
                x[i], x[j] = x[j], x[i]
                y[i], y[j] = y[j], y[i]
            assert all(x[i] <= x[i + 1] for i in range(n - 1)), "a is not sorted"
            assert all(y[i] <= y[i + 1] for i in range(n - 1)), "b is not sorted"

    return check
