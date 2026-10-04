# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n, m = (data[0], data[1])
adj = [[] for _ in range(n + 1)]
p = 2
for _ in range(n - 1):
    a, b = (data[p], data[p + 1])
    p += 2
    adj[a].append(b)
    adj[b].append(a)
special = [False] * (n + 1)
for x in data[p:p + m]:
    special[x] = True
deg = [len(adj[i]) for i in range(n + 1)]
alive = [True] * (n + 1)
q = deque()
for i in range(1, n + 1):
    if deg[i] <= 1 and (not special[i]):
        q.append(i)
while q:
    v = q.popleft()
    if not alive[v]:
        continue
    alive[v] = False
    for u in adj[v]:
        if alive[u]:
            deg[u] -= 1
            if deg[u] == 1 and (not special[u]):
                q.append(u)
edges = sum((deg[i] for i in range(1, n + 1) if alive[i])) // 2

def farthest(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    best = start
    while q:
        v = q.popleft()
        if dist[v] > dist[best] or (dist[v] == dist[best] and v < best):
            best = v
        for u in adj[v]:
            if alive[u] and dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(u)
    return (best, dist)
start = next((i for i in range(1, n + 1) if alive[i]))
a, _ = farthest(start)
b, da = farthest(a)
c, db = farthest(b)
diam = da[b]
ans = min((i for i in range(1, n + 1) if alive[i] and max(da[i], db[i]) == diam))
print(ans)
print(2 * edges - diam)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
