import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
tin = [0] * (n + 1)
tout = [0] * (n + 1)
timer = 0

stack = [(1, 1, 0)]
parent[1] = 1

while stack:
    v, p, state = stack.pop()
    if state == 0:
        timer += 1
        tin[v] = timer
        stack.append((v, p, 1))
        for to in g[v]:
            if to != p:
                parent[to] = v
                depth[to] = depth[v] + 1
                stack.append((to, v, 0))
    else:
        tout[v] = timer

def is_ancestor(a, b):
    return tin[a] <= tin[b] <= tout[a]

ans = []

for _ in range(m):
    q = list(map(int, input().split()))
    vertices = q[1:]

    deepest = vertices[0]
    for v in vertices:
        if depth[v] > depth[deepest]:
            deepest = v

    ok = True
    for v in vertices:
        if not is_ancestor(parent[v], deepest):
            ok = False
            break

    ans.append("YES" if ok else "NO")

print("\n".join(ans))
