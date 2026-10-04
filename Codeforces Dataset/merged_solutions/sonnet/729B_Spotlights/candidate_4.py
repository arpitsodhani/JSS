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
    rows_total = [sum(row) for row in grid]
    cols_total = [0] * m
    for row in grid:
        for j in range(m):
            cols_total[j] += row[j]
    total = 0
    above = [0] * m
    for i in range(n):
        row = grid[i]
        before = 0
        for j in range(m):
            if row[j] == 0:
                if before:
                    total += 1
                if rows_total[i] - before:
                    total += 1
                if above[j]:
                    total += 1
                if cols_total[j] - above[j]:
                    total += 1
            else:
                before += 1
        for j in range(m):
            above[j] += row[j]
    return total

# --- clause: main :: () -> None ---
def main():
    n, m, grid = read_input()
    sys.stdout.write(str(count_positions(n, m, grid)) + "\n")


if __name__ == "__main__":
    main()
