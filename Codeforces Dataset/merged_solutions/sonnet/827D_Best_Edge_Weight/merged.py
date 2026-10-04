# Clause setup_environment [Confidence: 0.60]
import sys

def main():
    buf = sys.stdin.buffer.read().split()
    if not buf:
        return
    n = int(buf[0])
    m = int(buf[1])
    all_edges = []
    k = 2
    for edge_id in range(m):
        x = int(buf[k])
        y = int(buf[k + 1])
        z = int(buf[k + 2])
        k += 3
        all_edges.append((z, x, y, edge_id))


# Clause solve_logic [Confidence: 0.80]
    dsu = list(range(n + 1))
    rank = [1] * (n + 1)

    def root(x):
        while dsu[x] != x:
            dsu[x] = dsu[dsu[x]]
            x = dsu[x]
        return x

    def merge(a, b):
        a = root(a)
        b = root(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        dsu[b] = a
        rank[a] += rank[b]
        return True

    tree = [[] for _ in range(n + 1)]
    used = [False] * m
    for w, u, v, i in sorted(edges):
        if merge(u, v):
            used[i] = True
            tree[u].append((v, w, i))
            tree[v].append((u, w, i))

    lg = (n + 1).bit_length()
    up = [[0] * (n + 1) for _ in range(lg)]
    mx = [[0] * (n + 1) for _ in range(lg)]
    depth = [0] * (n + 1)
    pedge = [-1] * (n + 1)
    stack = [1]
    seen = [False] * (n + 1)
    seen[1] = True
    order = []
    while stack:
        x = stack.pop()
        order.append(x)
        for y, w, eid in tree[x]:
            if not seen[y]:
                seen[y] = True
                depth[y] = depth[x] + 1
                up[0][y] = x
                mx[0][y] = w
                pedge[y] = eid
                stack.append(y)

    for j in range(1, lg):
        uj = up[j]
        ujm = up[j - 1]
        mj = mx[j]
        mjm = mx[j - 1]
        for v in range(1, n + 1):
            mid = ujm[v]
            uj[v] = ujm[mid]
            mj[v] = max(mjm[v], mjm[mid])

    def max_path(a, b):
        res = 0
        if depth[a] < depth[b]:
            a, b = b, a
        diff = depth[a] - depth[b]
        bit = 0
        while diff:
            if diff & 1:
                res = max(res, mx[bit][a])
                a = up[bit][a]
            diff >>= 1
            bit += 1
        if a == b:
            return res
        for j in range(lg - 1, -1, -1):
            if up[j][a] != up[j][b]:
                res = max(res, mx[j][a], mx[j][b])
                a = up[j][a]
                b = up[j][b]
        return max(res, mx[0][a], mx[0][b])

    ans = [-1] * m
    jump = list(range(n + 1))

    def top(x):
        while jump[x] != x:
            jump[x] = jump[jump[x]]
            x = jump[x]
        return x

    for w, u, v, i in edges:
        if not used[i]:
            ans[i] = max_path(u, v) - 1

    for w, u, v, i in sorted(edges):
        if used[i]:
            continue
        a = top(u)
        b = top(v)
        while a != b:
            if depth[a] < depth[b]:
                a, b = b, a
            ans[pedge[a]] = w - 1
            jump[a] = top(up[0][a])
            a = top(a)


# Clause finish_program [Confidence: 0.60]
    sys.stdout.write(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()


