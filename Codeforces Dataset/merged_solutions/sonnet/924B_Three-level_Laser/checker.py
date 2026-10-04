"""924B prints a real number, so the checker compares against its own O(n^2)
scan with the 1e-9 tolerance the statement allows.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, u = data[0], data[1]
    e = data[2:2 + n]
    best = None
    for i in range(n):
        for k in range(i + 2, n):
            if e[k] - e[i] > u:
                break
            value = (e[k] - e[i + 1]) / (e[k] - e[i])
            if best is None or value > best:
                best = value

    def check(out):
        text = out.strip()
        if best is None:
            assert text == "-1", f"no triple fits, printed {text!r}"
            return
        assert text != "-1", "a triple exists but -1 was printed"
        got = float(text)
        assert abs(got - best) <= 1e-9 * max(1.0, abs(best)), (
            f"printed {got}, expected {best}")

    return check
