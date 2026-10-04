# CLAUSE: setup_environment
import sys
from bisect import bisect_left

# CLAUSE: solve_logic
data = sys.stdin.buffer.read().split()
if not data:
    sys.exit()
p = 0
n = int(data[p])
p += 1
m = int(data[p])
p += 1
k = int(data[p])
p += 1
blocks = set()
diag_diff = {}
diag_sum = {}
for _ in range(k):
    x = int(data[p])
    p += 1
    y = int(data[p])
    p += 1
    blocks.add((x, y))
    diag_diff.setdefault(x - y, []).append(x)
    diag_sum.setdefault(x + y, []).append(x)
for v in diag_diff.values():
    v.sort()
for v in diag_sum.values():
    v.sort()
x = int(data[p])
p += 1
y = int(data[p])
p += 1
s = data[p].decode()
dirs = {'NE': (-1, 1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (1, -1)}
dx, dy = dirs[s]

def blocked(r, c):
    return r < 1 or r > n or c < 1 or (c > m) or ((r, c) in blocks)
seen = set()
ans = 0
while True:
    state = (x, y, dx, dy)
    if state in seen:
        break
    seen.add(state)
    row_limit = n - x + 1 if dx == 1 else x
    col_limit = m - y + 1 if dy == 1 else y
    dist = row_limit if row_limit < col_limit else col_limit
    if dx == dy:
        arr = diag_diff.get(x - y)
    else:
        arr = diag_sum.get(x + y)
    if arr:
        idx = bisect_left(arr, x)
        bd = 10 ** 30
        if dx == 1:
            if idx < len(arr):
                bd = arr[idx] - x
        elif idx > 0:
            bd = x - arr[idx - 1]
        if bd > 0 and bd < dist:
            dist = bd
    ans += dist
    last_x = x + dx * (dist - 1)
    last_y = y + dy * (dist - 1)
    vx = last_x if dx == 1 else last_x - 1
    vy = last_y if dy == 1 else last_y - 1
    side_row = blocked(vx + 1 if dx == 1 else vx, vy if dy == 1 else vy + 1)
    side_col = blocked(vx if dx == 1 else vx + 1, vy + 1 if dy == 1 else vy)
    if side_row ^ side_col:
        if side_row:
            dx = -dx
        else:
            dy = -dy
    else:
        dx = -dx
        dy = -dy
    x = vx + 1 if dx == 1 else vx
    y = vy + 1 if dy == 1 else vy
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
