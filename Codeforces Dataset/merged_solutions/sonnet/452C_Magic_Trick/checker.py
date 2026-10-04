"""452C prints a probability, compared with a 1e-6 tolerance."""


def check_for(stdin, expected):
    target = float(expected.split()[0])

    def check(out):
        value = float(out.split()[0])
        error = abs(value - target)
        assert error <= 1e-6 or error <= 1e-6 * abs(target), f"expected {target}, got {value}"

    return check
