"""1288D accepts any pair of arrays whose element-wise maximum has the largest
possible minimum.

The checker recomputes the optimum by scanning candidate thresholds with the
same bitmask argument, but independently of the printed answer.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, m = data[0], data[1]
    rows = []
    pos = 2
    for _ in range(n):
        rows.append(data[pos:pos + m])
        pos += m
    values = sorted({v for row in rows for v in row})
    best = 0
    for limit in values:
        full = (1 << m) - 1
        masks = set()
        for row in rows:
            mask = 0
            for bit in range(m):
                if row[bit] >= limit:
                    mask |= 1 << bit
            masks.add(mask)
        ok = any((one | two) == full for one in masks for two in masks)
        if ok and limit > best:
            best = limit

    def check(out):
        i, j = (int(v) for v in out.split())
        assert 1 <= i <= n and 1 <= j <= n, "index out of range"
        got = min(max(rows[i - 1][k], rows[j - 1][k]) for k in range(m))
        assert got == best, f"pair gives {got}, the best is {best}"

    return check
