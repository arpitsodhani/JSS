# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
p = 0

n = data[p]
p += 1

parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

k = data[p]
p += 1
for _ in range(k):
    a = data[p] - 1
    b = data[p + 1] - 1
    p += 2
    union(a, b)

m = data[p]
p += 1

bad = [False] * n
dislikes = []
for _ in range(m):
    a = data[p] - 1
    b = data[p + 1] - 1
    p += 2
    dislikes.append((a, b))

for i in range(n):
    find(i)

for a, b in dislikes:
    if find(a) == find(b):
        bad[find(a)] = True

ans = 0
for i in range(n):
    if find(i) == i and not bad[i]:
        ans = max(ans, size[i])

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
