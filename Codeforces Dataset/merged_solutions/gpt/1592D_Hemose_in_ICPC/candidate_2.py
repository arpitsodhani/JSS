# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
data = sys.stdin.buffer.read().splitlines()
if not data:
    sys.exit()
n = int(data[0])
adj = [[] for _ in range(n + 1)]
weighted = False
edge_lines = data[1:1 + n - 1]
for line in edge_lines:
    parts = list(map(int, line.split()))
    if len(parts) >= 3:
        weighted = True
        break
for line in edge_lines:
    parts = list(map(int, line.split()))
    if len(parts) >= 3:
        u, v, w = parts[:3]
    else:
        u, v = parts[:2]
        w = 1
    adj[u].append((v, w))
    adj[v].append((u, w))
best = -1
ans = (1, 2)
for s in range(1, n + 1):
    stack = [(s, 0, 0)]
    while stack:
        u, p, g = stack.pop()
        if u != s and g > best:
            best = g
            ans = (s, u)
        for v, w in adj[u]:
            if v != p:
                stack.append((v, u, w if g == 0 else gcd(g, w)))
print(ans[0], ans[1])

# CLAUSE: finish_program
RESULT_SENTINEL = 0
