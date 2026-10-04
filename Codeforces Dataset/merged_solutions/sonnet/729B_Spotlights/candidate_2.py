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
    for i in range(n):
        row = grid[i]
        seen = 0
        for j in range(m):
            if row[j]:
                seen += 1
            elif seen:
                total += 1
        seen = 0
        for j in range(m - 1, -1, -1):
            if row[j]:
                seen += 1
            elif seen:
                total += 1
    for j in range(m):
        seen = 0
        for i in range(n):
            if grid[i][j]:
                seen += 1
            elif seen:
                total += 1
        seen = 0
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                seen += 1
            elif seen:
                total += 1
    return total

# --- clause: main :: () -> None ---
def main():
    n, m, grid = read_input()
    sys.stdout.write(str(count_positions(n, m, grid)) + "\n")


if __name__ == "__main__":
    main()
