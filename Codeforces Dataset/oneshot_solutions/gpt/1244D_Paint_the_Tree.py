import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(3)]

g = [[] for _ in range(n)]
deg = [0] * n

for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1
    deg[v] += 1

if any(d > 2 for d in deg):
    print(-1)
    sys.exit()

start = 0
for i in range(n):
    if deg[i] <= 1:
        start = i
        break

order = []
parent = -1
cur = start

while cur != -1:
    order.append(cur)
    nxt = -1
    for v in g[cur]:
        if v != parent:
            nxt = v
            break
    parent, cur = cur, nxt

best = 10**30
best_colors = None

for p in permutations(range(3)):
    total = 0
    colors = [0] * n
    for i, v in enumerate(order):
        c = p[i % 3]
        total += cost[c][v]
        colors[v] = c + 1
    if total < best:
        best = total
        best_colors = colors

print(best)
print(*best_colors)
