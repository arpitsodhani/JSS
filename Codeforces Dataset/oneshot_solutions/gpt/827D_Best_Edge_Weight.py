import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    edges = []
    p = 2
    for i in range(m):
        u, v, w = data[p], data[p + 1], data[p + 2]
        p += 3
        edges.append((u - 1, v - 1, w, i))

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return False
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        return True

    tree = [[] for _ in range(n)]
    in_mst = [False] * m

    for u, v, w, idx in sorted(edges, key=lambda x: x[2]):
        if union(u, v):
            in_mst[idx] = True
            tree[u].append((v, w, idx))
            tree[v].append((u, w, idx))

    log = (n).bit_length()
    up = [[-1] * n for _ in range(log)]
    depth = [0] * n
    tin = [0] * n
    tout = [0] * n
    edge_to_parent = [-1] * n
    order = []
    timer = 0

    stack = [(0, -1, 0)]
    while stack:
        v, par, state = stack.pop()
        if state == 0:
            tin[v] = timer
            timer += 1
            up[0][v] = par if par != -1 else v
            order.append(v)
            stack.append((v, par, 1))
            for to, w, idx in tree[v]:
                if to == par:
                    continue
                depth[to] = depth[v] + 1
                edge_to_parent[to] = idx
                stack.append((to, v, 0))
        else:
            tout[v] = timer

    for k in range(1, log):
        prev = up[k - 1]
        cur = up[k]
        for v in range(n):
            cur[v] = prev[prev[v]]

    def is_ancestor(a, b):
        return tin[a] <= tin[b] and tout[b] <= tout[a]

    def lca(a, b):
        if is_ancestor(a, b):
            return a
        if is_ancestor(b, a):
            return b
        for k in range(log - 1, -1, -1):
            x = up[k][a]
            if not is_ancestor(x, b):
                a = x
        return up[0][a]

    inf = 10 ** 30
    best = [inf] * n

    def add_path(v, anc, val):
        while v != anc:
            if best[v] <= val:
                break
            best[v] = val
            v = up[0][v]

    for u, v, w, idx in edges:
        if in_mst[idx]:
            continue
        a = lca(u, v)
        add_path(u, a, w)
        add_path(v, a, w)

    ans = [-1] * m
    for v in range(1, n):
        idx = edge_to_parent[v]
        if best[v] != inf:
            ans[idx] = best[v] - 1

    for u, v, w, idx in edges:
        if not in_mst[idx]:
            ans[idx] = w - 1

    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
