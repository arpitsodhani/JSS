t, sx, sy, ex, ey = map(int, input().split())
wind = input().strip()

dx = ex - sx
dy = ey - sy

if dx == 0 and dy == 0:
    print(0)
    exit()

for i in range(t):
    direction = wind[i]
    if direction == 'E' and dx > 0:
        dx -= 1
    elif direction == 'W' and dx < 0:
        dx += 1
    elif direction == 'N' and dy > 0:
        dy -= 1
    elif direction == 'S' and dy < 0:
        dy += 1
    
    if dx == 0 and dy == 0:
        print(i + 1)
        exit()

print(-1)
