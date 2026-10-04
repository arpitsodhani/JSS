"""1971C: the two chords of the clock face intersect or they do not.

The Codeforces page for this problem could not be fetched, so instead of trusting
a recorded answer the checker places the twelve numbers on a unit circle and runs
a real segment-intersection test.
"""
from math import cos, pi, sin


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    cases = [tuple(data[1 + 4 * i:5 + 4 * i]) for i in range(t)]

    def point(label):
        angle = pi / 2 - (label % 12) * pi / 6
        return cos(angle), sin(angle)

    def side(p, q, r):
        value = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        if value > 1e-9:
            return 1
        if value < -1e-9:
            return -1
        return 0

    def crosses(a, b, c, d):
        pa, pb, pc, pd = point(a), point(b), point(c), point(d)
        return (side(pa, pb, pc) * side(pa, pb, pd) < 0
                and side(pc, pd, pa) * side(pc, pd, pb) < 0)

    def check(out):
        words = out.split()
        assert len(words) == t, f"expected {t} answers, got {len(words)}"
        for (a, b, c, d), word in zip(cases, words):
            want = "YES" if crosses(a, b, c, d) else "NO"
            assert word.upper() == want, (
                f"({a}, {b}, {c}, {d}): printed {word}, the segments say {want}")

    return check
