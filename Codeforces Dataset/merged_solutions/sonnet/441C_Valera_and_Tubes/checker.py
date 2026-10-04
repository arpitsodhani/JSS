"""441C accepts any fancy arrangement: k tubes, each a self-avoiding path of at
least two orthogonally adjacent cells, together covering every cell exactly once."""


def check_for(stdin, expected):
    n, m, k = (int(v) for v in stdin.split())

    def check(out):
        got = [int(v) for v in out.split()]
        at = 0
        seen = set()
        for tube in range(k):
            assert at < len(got), f"tube {tube + 1} is missing"
            size = got[at]
            at += 1
            assert size >= 2, f"tube {tube + 1} has {size} cells, needs at least 2"
            cells = []
            for _ in range(size):
                x, y = got[at], got[at + 1]
                at += 2
                assert 1 <= x <= n and 1 <= y <= m, f"cell ({x}, {y}) is off the table"
                assert (x, y) not in seen, f"cell ({x}, {y}) is used twice"
                seen.add((x, y))
                cells.append((x, y))
            for a, b in zip(cells, cells[1:]):
                assert abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1, f"{a} and {b} are not adjacent"
        assert at == len(got), "trailing output"
        assert len(seen) == n * m, f"covered {len(seen)} cells of {n * m}"

    return check
