import sys


# --- clause: read_input :: () -> list[list[str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    offset = 1
    cases = []
    for _ in range(t):
        n = int(fields[offset])
        offset += 2
        grid = [fields[offset + i].decode() for i in range(n)]
        offset += n
        cases.append(grid)
    return cases


# --- clause: paint_board :: (grid: list[str]) -> list[list[str]] | None ---
def paint_board(grid):
    n = len(grid)
    m = len(grid[0])
    board = [list(row) for row in grid]
    out = [["."] * m for _ in range(n)]
    for i in range(n):
        spots = [j for j in range(m) if board[i][j] == "U"]
        if len(spots) % 2:
            return None
        for ranked in range(len(spots)):
            j = spots[ranked]
            top = "W" if ranked * 2 < len(spots) else "B"
            out[i][j] = top
            out[i + 1][j] = "B" if top == "W" else "W"
    for j in range(m):
        spots = [i for i in range(n) if board[i][j] == "L"]
        if len(spots) % 2:
            return None
        for ranked in range(len(spots)):
            i = spots[ranked]
            left = "W" if ranked * 2 < len(spots) else "B"
            out[i][j] = left
            out[i][j + 1] = "B" if left == "W" else "W"
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for grid in read_input():
        painted = paint_board(grid)
        if painted is None:
            out.append("-1")
        else:
            for row in painted:
                out.append("".join(row))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
