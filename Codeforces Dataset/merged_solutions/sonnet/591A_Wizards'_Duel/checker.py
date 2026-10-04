"""591A prints a real number; the checker allows the 1e-4 error the statement
grants.
"""


def check_for(stdin, expected):
    target = float(expected.strip())

    def check(out):
        value = float(out.strip())
        assert abs(value - target) <= 1e-4 * max(1.0, abs(target)), (
            f"printed {value}, expected {target}")

    return check
