"""416A accepts any y consistent with every answered question."""


def check_for(stdin, expected):
    tokens = stdin.split()
    n = int(tokens[0])
    rules = []
    for i in range(n):
        rules.append((tokens[1 + 3 * i], int(tokens[2 + 3 * i]), tokens[3 + 3 * i]))

    def holds(y, sign, x):
        if sign == ">":
            return y > x
        if sign == "<":
            return y < x
        if sign == ">=":
            return y >= x
        return y <= x

    lo, hi = -2 * 10 ** 9, 2 * 10 ** 9
    for sign, x, answer in rules:
        want = answer == "Y"
        if (sign == ">") == want and sign in (">",):
            lo = max(lo, x + 1)
        elif sign == ">" and not want:
            hi = min(hi, x)
        elif sign == "<" and want:
            hi = min(hi, x - 1)
        elif sign == "<" and not want:
            lo = max(lo, x)
        elif sign == ">=" and want:
            lo = max(lo, x)
        elif sign == ">=" and not want:
            hi = min(hi, x - 1)
        elif sign == "<=" and want:
            hi = min(hi, x)
        elif sign == "<=" and not want:
            lo = max(lo, x + 1)
    feasible = lo <= hi and lo <= 2 * 10 ** 9 and hi >= -2 * 10 ** 9

    def check(out):
        got = out.split()
        if got[0] == "Impossible":
            assert not feasible, "printed Impossible but a value exists"
            return
        assert feasible, "printed a value but none exists"
        y = int(got[0])
        assert -2 * 10 ** 9 <= y <= 2 * 10 ** 9, f"{y} outside the allowed range"
        for sign, x, answer in rules:
            assert holds(y, sign, x) == (answer == "Y"), (
                f"y={y} disagrees with '{sign} {x} {answer}'")

    return check
