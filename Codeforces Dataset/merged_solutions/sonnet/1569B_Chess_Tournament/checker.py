"""1569B accepts any tournament that meets everybody's expectations.

The reference output decides only whether a test case is possible; the matrix
itself is free, so this checks consistency (X on the diagonal, mirrored results)
and then each player's own wish.
"""


def check_for(stdin, expected):
    lines = stdin.split("\n")
    t = int(lines[0])
    wishes = []
    pos = 1
    for _ in range(t):
        pos += 1
        wishes.append(lines[pos].strip())
        pos += 1
    verdicts = [line.strip().upper() for line in expected.split("\n") if line.strip() in ("YES", "NO")]

    def check(out):
        rows = [line for line in out.split("\n") if line.strip()]
        at = 0
        for case in range(t):
            s = wishes[case]
            n = len(s)
            head = rows[at].strip().upper()
            at += 1
            assert head == verdicts[case], f"case {case + 1}: said {head}, expected {verdicts[case]}"
            if head == "NO":
                continue
            grid = [rows[at + i].strip() for i in range(n)]
            at += n
            for i in range(n):
                assert len(grid[i]) == n, f"case {case + 1}: row {i + 1} has {len(grid[i])} cells"
                assert grid[i][i] == "X", f"case {case + 1}: cell ({i + 1},{i + 1}) is not X"
                for j in range(n):
                    if i == j:
                        continue
                    pair = grid[i][j] + grid[j][i]
                    assert pair in ("+-", "-+", "=="), f"case {case + 1}: games {i + 1}-{j + 1} disagree"
            for i in range(n):
                if s[i] == "1":
                    assert "-" not in grid[i], f"case {case + 1}: player {i + 1} lost a game"
                else:
                    assert "+" in grid[i], f"case {case + 1}: player {i + 1} won nothing"

    return check
