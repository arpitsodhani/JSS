# CLAUSE: setup_environment
import sys
from array import array

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

n = next(it)
a = [next(it) for _ in range(n)]

cnt = a[:]
dist = []
ans = 0.0

for x in a:
    d = array('d', [0.0]) * (x + 1)
    d[x] = 1.0
    if x == 0:
        ans += 1.0
    dist.append(d)

q = next(it)
out = []

for _ in range(q):
    u = next(it) - 1
    v = next(it) - 1
    k = next(it)

    d = dist[u]
    old0 = d[0]
    total = cnt[u]

    for _ in range(k):
        nd = array('d', [0.0]) * len(d)
        inv = 1.0 / total
        limit = min(len(d) - 1, total - 1)

        for x in range(limit + 1):
            val = d[x] * (total - x)
            if x + 1 < len(d):
                val += d[x + 1] * (x + 1)
            nd[x] = val * inv

        d = nd
        total -= 1

    dist[u] = d
    ans += d[0] - old0

    cnt[u] -= k
    cnt[v] += k

    out.append(f"{ans:.12f}")

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
