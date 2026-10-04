"""1333A takes any colouring with B = W + 1, so the grid itself is measured.

B counts black cells touching a white one, W counts white cells touching a
black one; the reference output is only used for the board sizes.
"""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    sizes = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(t)]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        at = 0
        for n, m in sizes:
            grid = rows[at:at + n]
            at += n
            assert len(grid) == n, "not enough rows printed"
            black = 0
            white = 0
            for i in range(n):
                assert len(grid[i]) == m, f"row {i + 1} has {len(grid[i])} cells, expected {m}"
                for j in range(m):
                    assert grid[i][j] in "BW", "cells must be B or W"
                    mixed = False
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        y = i + di
                        x = j + dj
                        if 0 <= y < n and 0 <= x < m and grid[y][x] != grid[i][j]:
                            mixed = True
                    if mixed:
                        if grid[i][j] == "B":
                            black += 1
                        else:
                            white += 1
            assert black == white + 1, f"B={black}, W={white}"

    return check
