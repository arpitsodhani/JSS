"""700A prints a real number, so the answer only has to match numerically.

Codeforces allows an absolute or relative error of 1e-6 here.
"""


def check_for(stdin, expected):
    target = float(expected.split()[0])

    def check(out):
        value = float(out.split()[0])
        error = abs(value - target)
        assert error <= 1e-6 or error <= 1e-6 * abs(target), f"expected {target}, got {value}"

    return check
