"""820B accepts any triple of vertices whose angle is closest to a.

For a regular n-gon the angle at v2 subtending an arc of s sides is s*180/n
degrees, so the checker measures the printed triple that way and compares with
the best achievable deviation.
"""


def check_for(stdin, expected):
    n, a = (int(v) for v in stdin.split()[:2])
    best = min(abs(span * 180 - a * n) for span in range(1, n - 1))

    def check(out):
        v = [int(x) for x in out.split()]
        assert len(v) == 3, f"expected three vertices, got {len(v)}"
        assert len(set(v)) == 3, "the vertices must be distinct"
        assert all(1 <= x <= n for x in v), "vertex out of range"
        v1, v2, v3 = v
        span = (v3 - v1) % n
        span = min(span, n - span)
        # the arc between v1 and v3 that avoids v2
        forward = (v3 - v1) % n
        backward = (v1 - v3) % n
        between_forward = (v2 - v1) % n < forward
        arc = backward if between_forward else forward
        here = abs(arc * 180 - a * n)
        assert here == best, f"deviation {here / n} degrees, best is {best / n}"

    return check
