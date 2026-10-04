# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

root = min(range(n), key=lambda i: a[i])

edges = []
for _ in range(m):
    x, y, w = map(int, input().split())
    edges.append((w, x - 1, y - 1))

for i in range(n):
    if i != root:
        edges.append((a[root] + a[i], root, i))

edges.sort()

parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

ans = 0
used = 0

for w, u, v in edges:
    ru = find(u)
    rv = find(v)
    if ru != rv:
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        size[ru] += size[rv]
        ans += w
        used += 1
        if used == n - 1:
            break

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
