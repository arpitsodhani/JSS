# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
t = int(data[0])
sx = int(data[1])
sy = int(data[2])
ex = int(data[3])
ey = int(data[4])
wind = data[5]
x, y = (sx, sy)
for i, c in enumerate(wind, 1):
    if c == 'E' and x < ex:
        x += 1
    elif c == 'W' and x > ex:
        x -= 1
    elif c == 'N' and y < ey:
        y += 1
    elif c == 'S' and y > ey:
        y -= 1
    if x == ex and y == ey:
        print(i)
        break
else:
    print(-1)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
