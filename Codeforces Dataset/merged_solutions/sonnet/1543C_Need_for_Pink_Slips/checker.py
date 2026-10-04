"""1543C prints expected values, so the answers only have to match numerically.

Codeforces accepts an absolute or relative error of 1e-6 here; the reference
outputs carry twelve decimals, which is far more than that tolerance needs.
"""


def check_for(stdin, expected):
    wanted = [float(line) for line in expected.split()]

    def check(out):
        got = [float(line) for line in out.split()]
        assert len(got) == len(wanted), f"expected {len(wanted)} values, got {len(got)}"
        for value, target in zip(got, wanted):
            error = abs(value - target)
            assert error <= 1e-6 or error <= 1e-6 * abs(target), \
                f"expected {target}, got {value}"

    return check
