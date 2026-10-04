import sys


# --- clause: read_input :: () -> tuple[int, int, list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    grid = []
    pos = 2
    for _ in range(n):
        grid.append(data[pos:pos + m])
        pos += m
    return n, m, grid


# --- clause: count_positions :: (n: int, m: int, grid: list[list[int]]) -> int ---
def count_positions(n, m, grid):
    total = 0
    left = [[0] * m for _ in range(n)]
    right = [[0] * m for _ in range(n)]
    for i in range(n):
        row = grid[i]
        seen = 0
        for j in range(m):
            left[i][j] = seen
            seen += row[j]
        seen = 0
        for j in range(m - 1, -1, -1):
            right[i][j] = seen
            seen += row[j]
    up = [0] * m
    down = [[0] * m for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(m):
            down[i][j] = up[j]
            up[j] += grid[i][j]
    above = [0] * m
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                if left[i][j]:
                    total += 1
                if right[i][j]:
                    total += 1
                if above[j]:
                    total += 1
                if down[i][j]:
                    total += 1
            above[j] += grid[i][j]
    return total


# --- clause: main :: () -> None ---
def main():
    n, m, grid = read_input()
    sys.stdout.write(str(count_positions(n, m, grid)) + "\n")


if __name__ == "__main__":
    main()
