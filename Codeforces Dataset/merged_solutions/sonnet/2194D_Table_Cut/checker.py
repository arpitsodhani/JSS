"""2194D accepts any staircase cut reaching the largest product.

The printed path is replayed to split the table, and the two counts of ones are
multiplied and compared with the best possible balanced split.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        grid = []
        for _ in range(n):
            grid.append(data[pos:pos + m])
            pos += m
        cases.append((n, m, grid))

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        at = 0
        for n, m, grid in cases:
            printed = int(rows[at])
            path = rows[at + 1]
            at += 2
            assert len(path) == n + m, f"path has {len(path)} moves, expected {n + m}"
            assert path.count("D") == n and path.count("R") == m, "wrong number of moves"
            total = sum(sum(row) for row in grid)
            best = (total // 2) * (total - total // 2)
            left = 0
            column = 0
            row = 0
            for move in path:
                if move == "R":
                    column += 1
                else:
                    left += sum(grid[row][:column])
                    row += 1
            right = total - left
            assert left * right == printed, f"the path splits into {left}*{right}, printed {printed}"
            assert printed == best, f"product {printed}, the best is {best}"

    return check
