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
    column_seen = [0] * m
    for i in range(n):
        row = grid[i]
        running = 0
        for j in range(m):
            if row[j]:
                running += 1
            else:
                if running:
                    total += 1
                if column_seen[j]:
                    total += 1
        running = 0
        for j in range(m - 1, -1, -1):
            if row[j]:
                running += 1
            elif running:
                total += 1
        for j in range(m):
            column_seen[j] += row[j]
    column_seen = [0] * m
    for i in range(n - 1, -1, -1):
        row = grid[i]
        for j in range(m):
            if row[j] == 0 and column_seen[j]:
                total += 1
        for j in range(m):
            column_seen[j] += row[j]
    return total

# --- clause: main :: () -> None ---
def main():
    n, m, grid = read_input()
    sys.stdout.write(str(count_positions(n, m, grid)) + "\n")


if __name__ == "__main__":
    main()
