# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
p = 1

dist = []
for _ in range(n):
    dist.append(data[p:p + n])
    p += n

order = [x - 1 for x in data[p:p + n]]
active = [False] * n
ans = []

for k in reversed(order):
    active[k] = True

    dk = dist[k]
    for i in range(n):
        dik = dist[i][k]
        row = dist[i]
        for j in range(n):
            nd = dik + dk[j]
            if nd < row[j]:
                row[j] = nd

    total = 0
    verts = [i for i in range(n) if active[i]]
    for i in verts:
        row = dist[i]
        for j in verts:
            total += row[j]

    ans.append(total)

print(*reversed(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
