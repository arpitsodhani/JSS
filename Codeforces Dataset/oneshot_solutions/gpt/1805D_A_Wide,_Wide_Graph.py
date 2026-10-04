import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

def bfs(s):
    dist = [-1] * n
    dist[s] = 0
    q = deque([s])
    far = s
    while q:
        u = q.popleft()
        far = u
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return far, dist

a, _ = bfs(0)
b, da = bfs(a)
_, db = bfs(b)

cnt = [0] * (n + 1)
for i in range(n):
    cnt[max(da[i], db[i])] += 1

ans = []
cur = 1
for k in range(1, n + 1):
    cur += cnt[k - 1]
    if cur > n:
        cur = n
    ans.append(str(cur))

print(" ".join(ans))
