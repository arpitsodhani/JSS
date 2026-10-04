"""761D accepts any b whose differences compress to the given p.

The printed sequence is checked against the range [l, r], the differences have
to be distinct, and their ranks have to reproduce p.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, l, r = data[0], data[1], data[2]
    a = data[3:3 + n]
    p = data[3 + n:3 + 2 * n]
    possible = expected.strip() != "-1"

    def check(out):
        if not possible:
            assert out.strip() == "-1", "printed a sequence where none exists"
            return
        b = [int(v) for v in out.split()]
        assert b != [-1], "a sequence exists but -1 was printed"
        assert len(b) == n, f"expected {n} values, got {len(b)}"
        for i in range(n):
            assert l <= b[i] <= r, f"b[{i + 1}] = {b[i]} outside [{l}, {r}]"
        c = [b[i] - a[i] for i in range(n)]
        assert len(set(c)) == n, "the differences are not distinct"
        order = sorted(c)
        rank = {value: i + 1 for i, value in enumerate(order)}
        assert [rank[value] for value in c] == p, "the compressed sequence differs"

    return check
