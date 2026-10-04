import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    cells = []
    for i in range(m):
        cells.append((data[2 + 2 * i], data[3 + 2 * i]))
    return n, cells

# Clause completes_square [Confidence: 0.80]
def completes_square(grid, x, y, n):
    for cx in range(x - 2, x + 1):
        for cy in range(y - 2, y + 1):
            if cx < 1 or cy < 1 or cx + 2 > n or cy + 2 > n:
                continue
            black = 0
            for dx in range(3):
                for dy in range(3):
                    if grid[cx + dx][cy + dy] == 1:
                        black += 1
            if black == 9:
                return True
    return False

# Clause find_move [Confidence: 1.00]
def find_move(n, cells):
    grid = [[0] * (n + 3) for _ in range(n + 3)]
    for step in range(len(cells)):
        x, y = cells[step]
        grid[x][y] = 1
        if completes_square(grid, x, y, n):
            return step + 1
    return -1

# Clause main [Confidence: 1.00]
def main():
    n, cells = read_input()
    print(find_move(n, cells))


if __name__ == "__main__":
    main()

