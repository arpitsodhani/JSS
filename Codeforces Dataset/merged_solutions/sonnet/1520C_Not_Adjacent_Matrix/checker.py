"""1520C accepts any n*n matrix holding 1..n^2 once with no adjacent cells
holding numbers that differ by exactly one; only n=2 is impossible.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    sizes = data[1:1 + data[0]]

    def check(out):
        tokens = out.split()
        pos = 0
        for n in sizes:
            if n == 2:
                assert tokens[pos] == "-1", f"n=2 has no matrix, got {tokens[pos]!r}"
                pos += 1
                continue
            grid = []
            for _ in range(n):
                grid.append([int(v) for v in tokens[pos:pos + n]])
                pos += n
            flat = [v for row in grid for v in row]
            assert sorted(flat) == list(range(1, n * n + 1)), f"n={n}: not a permutation of 1..{n*n}"
            for r in range(n):
                for c in range(n):
                    if r + 1 < n:
                        assert abs(grid[r][c] - grid[r + 1][c]) != 1, f"n={n}: ({r},{c}) below"
                    if c + 1 < n:
                        assert abs(grid[r][c] - grid[r][c + 1]) != 1, f"n={n}: ({r},{c}) right"
        assert pos == len(tokens), "extra output"

    return check
