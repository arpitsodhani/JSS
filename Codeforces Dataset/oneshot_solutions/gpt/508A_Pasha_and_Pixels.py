import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, m, k = data[0], data[1], data[2]

grid = [[False] * (m + 2) for _ in range(n + 2)]

pos = 3
for move in range(1, k + 1):
    x, y = data[pos], data[pos + 1]
    pos += 2
    grid[x][y] = True

    for dx in (-1, 0):
        for dy in (-1, 0):
            r = x + dx
            c = y + dy
            if 1 <= r < n and 1 <= c < m:
                if grid[r][c] and grid[r + 1][c] and grid[r][c + 1] and grid[r + 1][c + 1]:
                    print(move)
                    sys.exit()

print(0)
