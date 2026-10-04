import sys
from collections import deque

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

p = 0
n = data[p]
m = data[p + 1]
p += 2

s = []
h = []
for i in range(m):
    s.append(data[p])
    h.append(data[p + 1])
    p += 2

a = [0] + data[p:p + n]

can_right = [[False] * (n + 2) for _ in range(m)]
can_left = [[False] * (n + 2) for _ in range(m)]

for i in range(m):
    hp = h[i]
    ok = True
    for pos in range(s[i], n + 1):
        if a[pos] < 0:
            if hp < -a[pos]:
                ok = False
            else:
                hp += a[pos]
        elif a[pos] > 0:
            hp += a[pos]
        can_right[i][pos] = ok

    hp = h[i]
    ok = True
    for pos in range(s[i], 0, -1):
        if a[pos] < 0:
            if hp < -a[pos]:
                ok = False
            else:
                hp += a[pos]
        elif a[pos] > 0:
            hp += a[pos]
        can_left[i][pos] = ok

mn = min(s)
mx = max(s)

for r in range(1, n + 1):
    start = (r + 1, r)
    q = deque([start])
    parent = {start: None}
    finish = None

    while q:
        L, R = q.popleft()
        if L <= mn and R >= mx:
            finish = (L, R)
            break

        empty = L > R
        for i in range(m):
            x = s[i]

            if x < L:
                end = r if empty else L - 1
                if can_right[i][end]:
                    ns = (x, R)
                    if ns not in parent:
                        parent[ns] = (L, R, i)
                        q.append(ns)

            if x > R:
                end = r if empty else R + 1
                if can_left[i][end]:
                    ns = (r if empty else L, x)
                    if ns not in parent:
                        parent[ns] = (L, R, i)
                        q.append(ns)

    if finish is not None:
        order = []
        cur = finish
        while parent[cur] is not None:
            pl, pr, idx = parent[cur]
            order.append(idx)
            cur = (pl, pr)
        order.reverse()

        used = [False] * m
        for idx in order:
            used[idx] = True
        for i in range(m):
            if not used[i]:
                order.append(i)

        print(r)
        print(*[x + 1 for x in order])
        sys.exit()

print(-1)
