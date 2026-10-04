import sys

MOD = 1000000007

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]

children = [[] for _ in range(n)]
idx = 1
for v in range(1, n):
    p = data[idx]
    idx += 1
    children[p].append(v)

color = data[idx:idx + n]

order = [0]
for u in order:
    order.extend(children[u])

dp0 = [0] * n
dp1 = [0] * n

for u in reversed(order):
    if color[u]:
        a, b = 0, 1
    else:
        a, b = 1, 0

    for v in children[u]:
        va, vb = dp0[v], dp1[v]
        na = a * (va + vb) % MOD
        nb = (b * (va + vb) + a * vb) % MOD
        a, b = na, nb

    dp0[u] = a
    dp1[u] = b

print(dp1[0] % MOD)
