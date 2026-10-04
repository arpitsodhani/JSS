import sys
from collections import deque

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
g = data[1:1 + n]
a = list(map(int, data[1 + n:1 + 2 * n]))

cur = [0] * n
chosen = [False] * n
q = deque(i for i in range(n) if a[i] == 0)

while q:
    v = q.popleft()
    if chosen[v] or cur[v] != a[v]:
        continue

    chosen[v] = True
    row = g[v]

    for to in range(n):
        if row[to] == '1' or to == v:
            cur[to] += 1
            if not chosen[to] and cur[to] == a[to]:
                q.append(to)

ans = [i + 1 for i in range(n) if chosen[i]]

print(len(ans))
if ans:
    print(*ans)
