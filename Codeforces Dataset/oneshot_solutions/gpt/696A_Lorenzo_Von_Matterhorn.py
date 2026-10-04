import sys
from collections import defaultdict

data = list(map(int, sys.stdin.buffer.read().split()))
q = data[0]
i = 1
cost = defaultdict(int)
ans = []

for _ in range(q):
    t = data[i]
    i += 1
    if t == 1:
        v, u, w = data[i], data[i + 1], data[i + 2]
        i += 3
        while v != u:
            if v > u:
                cost[v] += w
                v //= 2
            else:
                cost[u] += w
                u //= 2
    else:
        v, u = data[i], data[i + 1]
        i += 2
        s = 0
        while v != u:
            if v > u:
                s += cost[v]
                v //= 2
            else:
                s += cost[u]
                u //= 2
        ans.append(str(s))

sys.stdout.write("\n".join(ans))
