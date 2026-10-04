"""222C accepts any reduced form of the same fraction.

The printed sets have to multiply to the same fraction as the input and share
no common factor, so this compares prime exponent vectors.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, m = data[0], data[1]
    top = data[2:2 + n]
    bottom = data[2 + n:2 + n + m]

    def factor(values):
        counts = {}
        for value in values:
            step = 2
            while step * step <= value:
                while value % step == 0:
                    counts[step] = counts.get(step, 0) + 1
                    value //= step
                step += 1
            if value > 1:
                counts[value] = counts.get(value, 0) + 1
        return counts

    want_top = factor(top)
    want_bottom = factor(bottom)
    wanted = {}
    for prime in set(want_top) | set(want_bottom):
        wanted[prime] = want_top.get(prime, 0) - want_bottom.get(prime, 0)

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        counts = [int(v) for v in rows[0]]
        left = [int(v) for v in rows[1]]
        right = [int(v) for v in rows[2]]
        assert counts == [len(left), len(right)], "the printed sizes do not match the sets"
        assert 1 <= len(left) <= 10 ** 5 and 1 <= len(right) <= 10 ** 5, "set size out of range"
        assert all(1 <= v <= 10 ** 7 for v in left + right), "a printed value is out of range"
        got_top = factor(left)
        got_bottom = factor(right)
        for prime in set(got_top) | set(got_bottom) | set(wanted):
            here = got_top.get(prime, 0) - got_bottom.get(prime, 0)
            assert here == wanted.get(prime, 0), f"the fraction changed at prime {prime}"
        for prime in got_top:
            assert prime not in got_bottom, f"the fraction is still divisible by {prime}"

    return check
