import sys


# --- clause: read_input :: () -> list[list[str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cursor = 1
    cases = []
    for _ in range(t):
        n = int(numbers[cursor])
        cursor += 2
        grid = [numbers[cursor + i].decode() for i in range(n)]
        cursor += n
        cases.append(grid)
    return cases


# --- clause: paint_board :: (grid: list[str]) -> list[list[str]] | None ---
def paint_board(grid):
    n = len(grid)
    m = len(grid[0])
    out = [["."] * m for _ in range(n)]
    for i in range(n):
        seen = 0
        for j in range(m):
            if grid[i][j] != "U":
                continue
            seen += 1
        if seen % 2:
            return None
        used = 0
        for j in range(m):
            if grid[i][j] != "U":
                continue
            top = "W" if used < seen // 2 else "B"
            out[i][j] = top
            out[i + 1][j] = "W" if top == "B" else "B"
            used += 1
    for j in range(m):
        seen = 0
        for i in range(n):
            if grid[i][j] == "L":
                seen += 1
        if seen % 2:
            return None
        used = 0
        for i in range(n):
            if grid[i][j] != "L":
                continue
            left = "W" if used < seen // 2 else "B"
            out[i][j] = left
            out[i][j + 1] = "W" if left == "B" else "B"
            used += 1
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
