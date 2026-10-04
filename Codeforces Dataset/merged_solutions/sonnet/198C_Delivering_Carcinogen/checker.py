"""198C is judged to 1e-6, so compare numerically."""


def check_for(stdin, expected):
    want = float(expected.split()[0])

    def check(out):
        got = float(out.split()[0])
        assert abs(got - want) <= 1e-6 * max(1.0, abs(want)), f"got {got}, expected {want}"

    return check
