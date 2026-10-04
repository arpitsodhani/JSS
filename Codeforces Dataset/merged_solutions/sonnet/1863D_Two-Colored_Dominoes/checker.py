"""1863D accepts any beautiful painting of the dominoes."""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        pos += 2
        cases.append([data[pos + i] for i in range(n)])
        pos += n
    verdicts = []
    rows = [line.strip() for line in expected.split("\n") if line.strip()]
    at = 0
    for grid in cases:
        if rows[at] == "-1":
            verdicts.append(False)
            at += 1
        else:
            verdicts.append(True)
            at += len(grid)

    def check(out):
        lines = [line.strip() for line in out.split("\n") if line.strip()]
        spot = 0
        for case in range(t):
            grid = cases[case]
            n = len(grid)
            m = len(grid[0])
            if not verdicts[case]:
                assert lines[spot] == "-1", f"case {case + 1}: printed a painting where none exists"
                spot += 1
                continue
            assert lines[spot] != "-1", f"case {case + 1}: a painting exists"
            board = lines[spot:spot + n]
            spot += n
            for i in range(n):
                assert len(board[i]) == m, f"case {case + 1}: row {i + 1} has the wrong width"
                for j in range(m):
                    if grid[i][j] == ".":
                        assert board[i][j] == ".", f"case {case + 1}: empty cell painted"
                    else:
                        assert board[i][j] in "WB", f"case {case + 1}: domino cell not painted"
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == "U":
                        assert board[i][j] != board[i + 1][j], f"case {case + 1}: domino not split"
                    if grid[i][j] == "L":
                        assert board[i][j] != board[i][j + 1], f"case {case + 1}: domino not split"
            for i in range(n):
                assert board[i].count("W") == board[i].count("B"), f"case {case + 1}: row {i + 1} unbalanced"
            for j in range(m):
                column = [board[i][j] for i in range(n)]
                assert column.count("W") == column.count("B"), f"case {case + 1}: column {j + 1} unbalanced"

    return check
