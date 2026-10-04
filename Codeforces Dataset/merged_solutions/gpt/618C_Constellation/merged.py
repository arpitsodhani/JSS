# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
points = []
k = 1
for i in range(n):
    x = data[k]
    y = data[k + 1]
    k += 2
    points.append((x, y, i + 1))

points.sort()

a = points[0]
b = points[1]

for c in points[2:]:
    x1, y1, _ = a
    x2, y2, _ = b
    x3, y3, _ = c
    if (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) != 0:
        print(a[2], b[2], c[2])
        break

# CLAUSE: finish_program
RESULT_SENTINEL = None
