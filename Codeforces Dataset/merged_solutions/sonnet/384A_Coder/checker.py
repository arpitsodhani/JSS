"""384A accepts any maximal non-attacking placement of Coders."""


def check_for(stdin, expected):
    n = int(stdin.split()[0])
    best = int(expected.split("\n")[0])

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        count = int(rows[0])
        board = rows[1:1 + n]
        assert len(board) == n, f"expected {n} rows, got {len(board)}"
        placed = 0
        for i in range(n):
            assert len(board[i]) == n, f"row {i + 1} has {len(board[i])} cells"
            for j in range(n):
                assert board[i][j] in "C.", "cells must be C or ."
                if board[i][j] != "C":
                    continue
                placed += 1
                for di, dj in ((1, 0), (0, 1)):
                    y = i + di
                    x = j + dj
                    if y < n and x < n:
                        assert board[y][x] != "C", f"two Coders attack at ({i + 1},{j + 1})"
        assert placed == count, f"printed {count} but placed {placed}"
        assert count == best, f"placed {count}, the maximum is {best}"

    return check
