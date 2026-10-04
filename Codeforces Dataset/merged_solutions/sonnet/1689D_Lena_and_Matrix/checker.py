"""1689D accepts any cell minimising the distance to the farthest black cell."""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 2
        cases.append([data[pos + i] for i in range(n)])
        pos += n

    def check(out):
        rows_out = [line for line in out.split("\n") if line.strip()]
        assert len(rows_out) == t, f"expected {t} lines, got {len(rows_out)}"
        for case in range(t):
            grid = cases[case]
            n = len(grid)
            m = len(grid[0])
            blacks = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == "B"]
            a, b = (int(v) for v in rows_out[case].split())
            assert 1 <= a <= n and 1 <= b <= m, f"case {case + 1}: cell outside the grid"
            def farthest(x, y):
                return max(abs(x - i) + abs(y - j) for i, j in blacks)
            want = min(farthest(i, j) for i in range(n) for j in range(m))
            got = farthest(a - 1, b - 1)
            assert got == want, f"case {case + 1}: distance {got}, best is {want}"

    return check
