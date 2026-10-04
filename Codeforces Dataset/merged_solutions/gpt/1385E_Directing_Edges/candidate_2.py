# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
input = sys.stdin.readline
tc = int(input())
out = []
for _ in range(tc):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    edges = []
    for _ in range(m):
        typ, x, y = map(int, input().split())
        edges.append((typ, x, y))
        if typ == 1:
            graph[x].append(y)
            indeg[y] += 1
    q = deque((i for i in range(1, n + 1) if indeg[i] == 0))
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for to in graph[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)
    if len(order) != n:
        out.append('NO')
        continue
    pos = [0] * (n + 1)
    for i, v in enumerate(order):
        pos[v] = i
    out.append('YES')
    for typ, x, y in edges:
        if typ == 1 or pos[x] < pos[y]:
            out.append(f'{x} {y}')
        else:
            out.append(f'{y} {x}')
print('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
