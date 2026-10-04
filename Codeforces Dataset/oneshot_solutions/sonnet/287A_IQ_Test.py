grid = [input() for _ in range(4)]

found = any(
    sum(grid[i + di][j + dj] == '#' for di in range(2) for dj in range(2)) != 2
    for i in range(3)
    for j in range(3)
)

print("YES" if found else "NO")
