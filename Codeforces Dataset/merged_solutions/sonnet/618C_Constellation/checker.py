"""618C accepts any three stars forming a positive-area triangle with the rest
of the stars strictly outside it.

The checker recomputes the cross products: the triangle must be non-degenerate,
and every other point must be strictly on the outside of at least one edge.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    pts = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def check(out):
        idx = [int(v) for v in out.split()]
        assert len(idx) == 3, f"expected three indices, got {len(idx)}"
        assert len(set(idx)) == 3, "the three indices must be distinct"
        assert all(1 <= i <= n for i in idx), "index out of range"
        a, b, c = (pts[i - 1] for i in idx)
        assert cross(a, b, c) != 0, "the triangle is degenerate"
        sign = 1 if cross(a, b, c) > 0 else -1
        for j, p in enumerate(pts, start=1):
            if j in idx:
                continue
            inside = all(sign * cross(u, v, p) >= 0 for u, v in ((a, b), (b, c), (c, a)))
            assert not inside, f"star {j} at {p} is not strictly outside"

    return check
