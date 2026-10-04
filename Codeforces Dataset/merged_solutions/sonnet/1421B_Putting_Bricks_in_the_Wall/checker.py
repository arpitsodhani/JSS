"""1421B accepts any set of at most two flips that blocks both digits.

The checker applies the printed flips and then runs a flood fill for each digit
to confirm no route from S to F survives.
"""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        grid = [data[pos + i] for i in range(n)]
        pos += n
        cases.append((n, grid))

    def blocked(n, grid, digit):
        seen = [[False] * n for _ in range(n)]
        stack = [(0, 0)]
        seen[0][0] = True
        while stack:
            r, c = stack.pop()
            if r == n - 1 and c == n - 1:
                return False
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                    cell = grid[nr][nc]
                    if cell in ("S", "F") or cell == digit:
                        seen[nr][nc] = True
                        stack.append((nr, nc))
        return True

    def check(out):
        tokens = out.split()
        at = 0
        for n, grid in cases:
            count = int(tokens[at])
            at += 1
            assert 0 <= count <= 2, f"printed {count} flips"
            rows = [list(row) for row in grid]
            used = set()
            for _ in range(count):
                r = int(tokens[at])
                c = int(tokens[at + 1])
                at += 2
                assert 1 <= r <= n and 1 <= c <= n, f"cell ({r}, {c}) outside the grid"
                assert (r, c) not in ((1, 1), (n, n)), "S and F cannot be inverted"
                assert (r, c) not in used, f"cell ({r}, {c}) inverted twice"
                used.add((r, c))
                rows[r - 1][c - 1] = "1" if rows[r - 1][c - 1] == "0" else "0"
            fixed = ["".join(row) for row in rows]
            for digit in ("0", "1"):
                assert blocked(n, fixed, digit), f"a path of {digit}s still exists"
        assert at == len(tokens), "extra output"

    return check
