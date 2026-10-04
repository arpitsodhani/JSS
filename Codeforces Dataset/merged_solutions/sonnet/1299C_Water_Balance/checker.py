"""1299C prints real numbers, so the answer is compared numerically.

Codeforces allows an absolute or relative error of 1e-9 on each value.
"""


def check_for(stdin, expected):
    wanted = [float(v) for v in expected.split()]

    def check(out):
        got = [float(v) for v in out.split()]
        assert len(got) == len(wanted), f"expected {len(wanted)} values, got {len(got)}"
        for value, target in zip(got, wanted):
            error = abs(value - target)
            assert error <= 1e-9 or error <= 1e-9 * abs(target), f"expected {target}, got {value}"

    return check
