import sys


# --- clause: read_input :: () -> list[list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
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
        cases.append(grid)
    return cases


# --- clause: stabilize :: (grid: list[list[int]]) -> list[list[int]] ---
def stabilize(grid):
    n = len(grid)
    m = len(grid[0])
    result = [row[:] for row in grid]
    for i in range(n):
        for j in range(m):
            here = grid[i][j]
            top = -1
            if i > 0 and grid[i - 1][j] > top:
                top = grid[i - 1][j]
            if i + 1 < n and grid[i + 1][j] > top:
                top = grid[i + 1][j]
            if j > 0 and grid[i][j - 1] > top:
                top = grid[i][j - 1]
            if j + 1 < m and grid[i][j + 1] > top:
                top = grid[i][j + 1]
            if here > top:
                result[i][j] = top
    return result


# --- clause: main :: () -> None ---
def main():
    out = []
    for grid in read_input():
        for row in stabilize(grid):
            out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
