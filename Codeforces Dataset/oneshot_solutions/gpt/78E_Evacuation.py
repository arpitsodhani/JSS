import sys
from collections import deque

data = sys.stdin.read().splitlines()
p = 0
while p < len(data) and data[p].strip() == "":
    p += 1
n, t = map(int, data[p].split())
p += 1

a = []
while len(a) < n:
    if data[p].strip() != "":
        a.append(data[p].strip())
    p += 1

b = []
while len(b) < n:
    if data[p].strip() != "":
        b.append(data[p].strip())
    p += 1

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
inf = 10 ** 9

bad = None
for i in range(n):
    for j in range(n):
        if a[i][j] == "Z":
            bad = (i, j)

poison = [[inf] * n for _ in range(n)]
q = deque([bad])
poison[bad[0]][bad[1]] = 0
while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and poison[nx][ny] == inf:
            if a[nx][ny] != "Y" and a[nx][ny] != "Z":
                poison[nx][ny] = poison[x][y] + 1
                q.append((nx, ny))

sources = []
capsules = []
for i in range(n):
    for j in range(n):
        if a[i][j].isdigit() and int(a[i][j]) > 0:
            sources.append((i, j, int(a[i][j])))
        if b[i][j].isdigit() and int(b[i][j]) > 0:
            capsules.append((i, j, int(b[i][j])))

s_cnt = len(sources)
c_cnt = len(capsules)
src = s_cnt + c_cnt
sink = src + 1
g = [[] for _ in range(sink + 1)]

def add_edge(v, u, cap):
    g[v].append([u, cap, len(g[u])])
    g[u].append([v, 0, len(g[v]) - 1])

for i, (_, _, cnt) in enumerate(sources):
    add_edge(src, i, cnt)

for j, (_, _, cnt) in enumerate(capsules):
    add_edge(s_cnt + j, sink, cnt)

cap_index = {(x, y): j for j, (x, y, _) in enumerate(capsules)}

for si, (sx, sy, _) in enumerate(sources):
    dist = [[-1] * n for _ in range(n)]
    dq = deque()
    if poison[sx][sy] >= 0:
        dist[sx][sy] = 0
        dq.append((sx, sy))
    while dq:
        x, y = dq.popleft()
        d = dist[x][y]
        if (x, y) in cap_index and d <= t and d <= poison[x][y]:
            add_edge(si, s_cnt + cap_index[(x, y)], inf)
        if d == t:
            continue
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            nd = d + 1
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                if a[nx][ny] != "Y" and a[nx][ny] != "Z" and nd <= poison[nx][ny]:
                    dist[nx][ny] = nd
                    dq.append((nx, ny))

flow = 0
while True:
    parent = [None] * (sink + 1)
    q = deque([src])
    parent[src] = (-1, -1)
    while q and parent[sink] is None:
        v = q.popleft()
        for i, e in enumerate(g[v]):
            if e[1] > 0 and parent[e[0]] is None:
                parent[e[0]] = (v, i)
                q.append(e[0])
                if e[0] == sink:
                    break
    if parent[sink] is None:
        break
    add = inf
    v = sink
    while v != src:
        pv, ei = parent[v]
        add = min(add, g[pv][ei][1])
        v = pv
    v = sink
    while v != src:
        pv, ei = parent[v]
        e = g[pv][ei]
        e[1] -= add
        g[v][e[2]][1] += add
        v = pv
    flow += add

print(flow)
