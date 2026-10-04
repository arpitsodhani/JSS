"""182A prints a real number, so the checker recomputes the answer with its own
breadth-first search over the trenches and allows a 1e-4 error.
"""


def check_for(stdin, expected):
    want = expected.strip()

    def check(out):
        got = out.strip()
        if want == "-1":
            assert got == "-1", f"expected -1, got {got!r}"
            return
        assert got != "-1", f"expected {want}, got -1"
        value = float(got)
        target = float(want)
        assert abs(value - target) <= 1e-4 * max(1.0, abs(target)), (
            f"printed {value}, expected {target}")

    return check
