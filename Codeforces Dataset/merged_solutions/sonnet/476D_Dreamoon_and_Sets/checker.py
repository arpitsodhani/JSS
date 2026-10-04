"""476D accepts any minimal-m family of n four-element sets of rank k.

Scaling by k, each set needs four pairwise coprime values, and six consecutive
integers hold exactly one such quadruple, so m = k(6n-1) is optimal.
"""


def check_for(stdin, expected):
    n, k = (int(v) for v in stdin.split())

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def check(out):
        got = [int(v) for v in out.split()]
        m = got[0]
        assert m == k * (6 * n - 1), f"m={m}, the minimum is {k * (6 * n - 1)}"
        values = got[1:]
        assert len(values) == 4 * n, f"expected {4 * n} numbers, got {len(values)}"
        used = set()
        for i in range(n):
            block = values[4 * i:4 * i + 4]
            for v in block:
                assert 1 <= v <= m, f"{v} outside [1, {m}]"
                assert v not in used, f"{v} is reused"
                used.add(v)
            for x in range(4):
                for y in range(x + 1, 4):
                    g = gcd(block[x], block[y])
                    assert g == k, f"gcd({block[x]}, {block[y]}) = {g}, expected {k}"

    return check
