# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
pts = [(data[i], data[i + 1]) for i in range(1, len(data), 2)]
xs = [x for x, y in pts]
ys = [y for x, y in pts]
candidates = set()
for x0 in (min(xs), max(xs) - n):
    for y0 in (min(ys), max(ys) - n):
        candidates.add((x0, y0))
for x0, y0 in candidates:
    x1 = x0 + n
    y1 = y0 + n
    bad = []
    for x, y in pts:
        on_boundary = x0 <= x <= x1 and y0 <= y <= y1 and (x == x0 or x == x1 or y == y0 or (y == y1))
        if not on_boundary:
            bad.append((x, y))
    if len(bad) == 1:
        print(bad[0][0], bad[0][1])
        break

# CLAUSE: finish_program
RESULT_SENTINEL = 0
