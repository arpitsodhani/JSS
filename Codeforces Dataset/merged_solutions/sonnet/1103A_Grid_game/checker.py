"""1103A accepts any legal run of placements, so replay the game.

Each tile must fit inside the 4x4 grid on free cells; after every placement,
every fully occupied row and every fully occupied column clears at once.
"""


def check_for(stdin, expected):
    tiles = stdin.split()[0]

    def check(out):
        got = [int(v) for v in out.split()]
        assert len(got) == 2 * len(tiles), f"expected {len(tiles)} placements"
        grid = [[0] * 4 for _ in range(4)]
        for step, kind in enumerate(tiles):
            r, c = got[2 * step] - 1, got[2 * step + 1] - 1
            cells = [(r, c), (r, c + 1)] if kind == "1" else [(r, c), (r + 1, c)]
            for x, y in cells:
                assert 0 <= x < 4 and 0 <= y < 4, f"tile {step + 1} leaves the grid at ({x + 1}, {y + 1})"
                assert grid[x][y] == 0, f"tile {step + 1} overlaps at ({x + 1}, {y + 1})"
                grid[x][y] = 1
            full_rows = [x for x in range(4) if all(grid[x])]
            full_cols = [y for y in range(4) if all(grid[x][y] for x in range(4))]
            for x in full_rows:
                for y in range(4):
                    grid[x][y] = 0
            for y in full_cols:
                for x in range(4):
                    grid[x][y] = 0

    return check
