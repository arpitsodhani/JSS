# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10 ** 9 + 7
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()
n = data[0]
v = data[1:1 + n]
edges = data[1 + n:]
g = [[] for _ in range(n)]
for i in range(0, 2 * (n - 1), 2):
    a = edges[i] - 1
    b = edges[i + 1] - 1
    g[a].append(b)
    g[b].append(a)
parent = [-1] * n
order = [0]
parent[0] = -2
for x in order:
    for y in g[x]:
        if y != parent[x]:
            parent[y] = x
            order.append(y)
sz = [1] * n
sub = [1] * n
for x in reversed(order):
    s = 1
    a = 1
    for y in g[x]:
        if parent[y] == x:
            s += sz[y]
            a -= sub[y]
    sz[x] = s
    sub[x] = a
tot = [0] * n
tot[0] = sub[0]
for x in order:
    for y in g[x]:
        if parent[y] == x:
            tot[y] = -tot[x]
ans = 0
for x in range(n):
    coef = n
    for y in g[x]:
        if parent[y] == x:
            comp_size = sz[y]
            comp_sum = -sub[y]
        else:
            comp_size = n - sz[x]
            comp_sum = tot[x] - 1 + sum((sub[z] for z in g[x] if parent[z] == x))
        coef += comp_sum * (n - comp_size)
    ans = (ans + v[x] % MOD * (coef % MOD)) % MOD
print(ans % MOD)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
