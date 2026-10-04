import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
idx = 2

ops = []
children = [[] for _ in range(n + 1)]
has_parent = [False] * (n + 1)

for _ in range(m):
    t = data[idx]
    idx += 1
    if t == 1:
        x = data[idx]
        y = data[idx + 1]
        idx += 2
        ops.append((1, x, y))
        children[y].append(x)
        has_parent[x] = True
    elif t == 2:
        x = data[idx]
        idx += 1
        ops.append((2, x))
    else:
        x = data[idx]
        y = data[idx + 1]
        idx += 2
        ops.append((3, x, y))

tin = [0] * (n + 1)
tout = [0] * (n + 1)
timer = 0

for root in range(1, n + 1):
    if has_parent[root]:
        continue
    stack = [(root, 0)]
    while stack:
        v, state = stack.pop()
        if state == 0:
            tin[v] = timer
            timer += 1
            stack.append((v, 1))
            for u in reversed(children[v]):
                stack.append((u, 0))
        else:
            tout[v] = timer - 1

parent = list(range(n + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

doc_v = [0]
doc_root = [0]
ans = []

for op in ops:
    if op[0] == 1:
        _, x, y = op
        parent[find(x)] = find(y)
    elif op[0] == 2:
        _, x = op
        doc_v.append(x)
        doc_root.append(find(x))
    else:
        _, x, k = op
        v = doc_v[k]
        r = doc_root[k]
        if tin[x] <= tin[v] <= tout[x] and tin[r] <= tin[x] <= tout[r]:
            ans.append("YES")
        else:
            ans.append("NO")

sys.stdout.write("\n".join(ans))
