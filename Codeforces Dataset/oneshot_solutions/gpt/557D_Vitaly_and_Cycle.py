import sys
from collections import deque

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
g = [[] for _ in range(n)]

idx = 2
for _ in range(m):
    u = data[idx] - 1
    v = data[idx + 1] - 1
    idx += 2
    g[u].append(v)
    g[v].append(u)

color = [-1] * n
ans = 0
has_large_component = False

for s in range(n):
    if color[s] != -1 or not g[s]:
        continue

    q = deque([s])
    color[s] = 0
    cnt = [1, 0]
    ok = True

    while q:
        u = q.popleft()
        for v in g[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                cnt[color[v]] += 1
                q.append(v)
            elif color[v] == color[u]:
                print(0, 1)
                sys.exit()

    if cnt[0] + cnt[1] >= 3:
        has_large_component = True
    ans += cnt[0] * (cnt[0] - 1) // 2 + cnt[1] * (cnt[1] - 1) // 2

if has_large_component:
    print(1, ans)
elif m > 0:
    print(2, m * (n - 2))
else:
    print(3, n * (n - 1) * (n - 2) // 6)
