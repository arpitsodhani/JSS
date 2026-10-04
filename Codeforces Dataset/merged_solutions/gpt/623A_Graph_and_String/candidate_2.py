# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()
n, m = (data[0], data[1])
adj = [[False] * n for _ in range(n)]
p = 2
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    adj[u][v] = True
    adj[v][u] = True
comp = [[] for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if not adj[i][j]:
            comp[i].append(j)
            comp[j].append(i)
color = [-1] * n
ok = True
for i in range(n):
    if comp[i] and color[i] == -1:
        color[i] = 0
        q = deque([i])
        while q and ok:
            v = q.popleft()
            for to in comp[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                elif color[to] == color[v]:
                    ok = False
                    break
if not ok:
    print('No')
    sys.exit()
s = ['b'] * n
for i in range(n):
    if color[i] == 0:
        s[i] = 'a'
    elif color[i] == 1:
        s[i] = 'c'
for i in range(n):
    for j in range(i + 1, n):
        need = not (s[i] == 'a' and s[j] == 'c' or (s[i] == 'c' and s[j] == 'a'))
        if adj[i][j] != need:
            print('No')
            sys.exit()
print('Yes')
print(''.join(s))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
