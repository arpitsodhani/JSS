def check_3x3_at(grid, n, r, c):
    if r < 0 or c < 0 or r + 2 >= n or c + 2 >= n:
        return False
    for dr in range(3):
        for dc in range(3):
            if not grid[r + dr][c + dc]:
                return False
    return True

def has_3x3_square_around(grid, n, x, y):
    for dr in range(-2, 1):
        for dc in range(-2, 1):
            if check_3x3_at(grid, n, x + dr, y + dc):
                return True
    return False

n, m = map(int, input().split())
grid = [[False] * n for _ in range(n)]

for move in range(1, m + 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    grid[x][y] = True
    
    if has_3x3_square_around(grid, n, x, y):
        print(move)
        exit()

print(-1)
