# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
f = [x - 1 for x in data[1:1 + n]]

sys.setrecursionlimit(1000000)

g = [[] for _ in range(n)]
rg = [[] for _ in range(n)]
for i, v in enumerate(f):
    g[i].append(v)
    rg[v].append(i)

vis = [False] * n
order = []

def dfs1(v):
    vis[v] = True
    for to in g[v]:
        if not vis[to]:
            dfs1(to)
    order.append(v)

for i in range(n):
    if not vis[i]:
        dfs1(i)

comp = [-1] * n
reps = []

def dfs2(v, c):
    comp[v] = c
    for to in rg[v]:
        if comp[to] == -1:
            dfs2(to, c)

for v in reversed(order):
    if comp[v] == -1:
        reps.append(v)
        dfs2(v, len(reps) - 1)

m = len(reps)
if m == 1:
    print(0)
    sys.exit()

indeg = [0] * m
outdeg = [0] * m

for i in range(n):
    a = comp[i]
    b = comp[f[i]]
    if a != b:
        outdeg[a] += 1
        indeg[b] += 1

sources = [i for i in range(m) if indeg[i] == 0]
sinks = [i for i in range(m) if outdeg[i] == 0]

k = max(len(sources), len(sinks))
ans = []

for i in range(k):
    a = sinks[i % len(sinks)]
    b = sources[(i + 1) % len(sources)]
    ans.append((reps[a] + 1, reps[b] + 1))

print(k)
for x, y in ans:
    print(x, y)

# CLAUSE: finish_program
RESULT_SENTINEL = None
