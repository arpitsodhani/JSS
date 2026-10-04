"""1293B is judged to 1e-4, so compare numerically rather than textually.

The best scenario eliminates exactly one opponent per question, so the prize is
the harmonic number 1 + 1/2 + ... + 1/n.
"""


def check_for(stdin, expected):
    n = int(stdin.split()[0])
    want = 0.0
    for i in range(1, n + 1):
        want += 1.0 / i

    def check(out):
        got = float(out.split()[0])
        assert abs(got - want) / max(1.0, abs(want)) <= 1e-6, f"got {got}, expected {want}"

    return check
