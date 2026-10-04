# CLAUSE: setup_environment
import sys
import math
from collections import deque

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()
it = iter(data)
a = next(it)
b = next(it)
ax = next(it)
ay = next(it)
bx = next(it)
by = next(it)
n = next(it)
seg = []
for _ in range(n):
    x1 = next(it)
    y1 = next(it)
    x2 = next(it)
    y2 = next(it)
    if x1 > x2 or y1 > y2:
        x1, x2 = (x2, x1)
        y1, y2 = (y2, y1)
    seg.append((x1, y1, x2, y2))

def point_seg_dist2(px, py, s):
    x1, y1, x2, y2 = s
    if x1 == x2:
        dx = px - x1
        if py < y1:
            dy = py - y1
        elif py > y2:
            dy = py - y2
        else:
            dy = 0
    else:
        dy = py - y1
        if px < x1:
            dx = px - x1
        elif px > x2:
            dx = px - x2
        else:
            dx = 0
    return dx * dx + dy * dy

def seg_dist2(s1, s2):
    x1, y1, x2, y2 = s1
    x3, y3, x4, y4 = s2
    if x1 == x2 and y3 == y4:
        if x3 <= x1 <= x4 and y1 <= y3 <= y2:
            return 0
    if y1 == y2 and x3 == x4:
        if x1 <= x3 <= x2 and y3 <= y1 <= y4:
            return 0
    return min(point_seg_dist2(x1, y1, s2), point_seg_dist2(x2, y2, s2), point_seg_dist2(x3, y3, s1), point_seg_dist2(x4, y4, s1))
limit = a * a
inf = float('inf')
ans = inf
direct2 = (ax - bx) * (ax - bx) + (ay - by) * (ay - by)
if direct2 <= limit:
    ans = math.sqrt(direct2)
dist = [-1] * n
q = deque()
for i, s in enumerate(seg):
    if point_seg_dist2(ax, ay, s) <= limit:
        dist[i] = 1
        q.append(i)
while q:
    v = q.popleft()
    d2b = point_seg_dist2(bx, by, seg[v])
    if d2b <= limit:
        ans = min(ans, dist[v] * (a + b) + math.sqrt(d2b))
    for u in range(n):
        if dist[u] == -1 and seg_dist2(seg[v], seg[u]) <= limit:
            dist[u] = dist[v] + 1
            q.append(u)
if ans == inf:
    print(-1)
else:
    print('{:.10f}'.format(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
