import sys


# --- clause: read_input :: () -> list[list[list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        m = fields[offset + 1]
        offset += 2
        grid = []
        for _ in range(n):
            grid.append(fields[offset:offset + m])
            offset += m
        cases.append(grid)
    return cases


# --- clause: stabilize :: (grid: list[list[int]]) -> list[list[int]] ---
def stabilize(grid):
    n = len(grid)
    m = len(grid[0])
    answer = [row[:] for row in grid]
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
                answer[i][j] = top
    return answer


# --- clause: main :: () -> None ---
def main():
    out = []
    for grid in read_input():
        for row in stabilize(grid):
            out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
