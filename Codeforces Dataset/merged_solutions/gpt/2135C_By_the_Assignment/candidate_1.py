# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 998244353

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    ans = []

    for _ in range(t):
        n = next(it)
        m = next(it)
        V = next(it)

        a = [next(it) for _ in range(n)]
        adj = [[] for _ in range(n)]
        eu = [0] * m
        ev = [0] * m

        for i in range(m):
            u = next(it) - 1
            v = next(it) - 1
            eu[i] = u
            ev[i] = v
            adj[u].append((v, i))
            adj[v].append((u, i))

        parent = [0] * n
        depth = [0] * n
        pedge = [-1] * n
        tree = [False] * m
        seen = [False] * n

        stack = [0]
        seen[0] = True
        while stack:
            v = stack.pop()
            for to, eid in adj[v]:
                if eid == pedge[v]:
                    continue
                if not seen[to]:
                    seen[to] = True
                    parent[to] = v
                    depth[to] = depth[v] + 1
                    pedge[to] = eid
                    tree[eid] = True
                    stack.append(to)

        log = n.bit_length()
        up = [parent[:]]
        for _ in range(1, log):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(x, y):
            if depth[x] < depth[y]:
                x, y = y, x
            d = depth[x] - depth[y]
            bit = 0
            while d:
                if d & 1:
                    x = up[bit][x]
                d >>= 1
                bit += 1
            if x == y:
                return x
            for k in range(log - 1, -1, -1):
                if up[k][x] != up[k][y]:
                    x = up[k][x]
                    y = up[k][y]
            return parent[x]

        dsu = list(range(n))
        size = [1] * n
        zero = [False] * n

        def find(x):
            while dsu[x] != x:
                dsu[x] = dsu[dsu[x]]
                x = dsu[x]
            return x

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return x
            if size[x] < size[y]:
                x, y = y, x
            dsu[y] = x
            size[x] += size[y]
            zero[x] |= zero[y]
            return x

        jump = list(range(n))

        def get(x):
            while jump[x] != x:
                jump[x] = jump[jump[x]]
                x = jump[x]
            return x

        def merge_path(x, anc):
            x = get(x)
            while depth[x] > depth[anc]:
                union(x, parent[x])
                jump[x] = get(parent[x])
                x = get(x)

        for eid in range(m):
            if tree[eid]:
                continue
            u = eu[eid]
            v = ev[eid]
            w = lca(u, v)
            merge_path(u, w)
            merge_path(v, w)
            if (depth[u] + depth[v] + 1) & 1:
                zero[find(u)] = True

        ok = True
        fixed = {}

        for i, val in enumerate(a):
            if val == -1:
                continue
            r = find(i)
            if zero[r] and val != 0:
                ok = False
                break
            if r in fixed:
                if fixed[r] != val:
                    ok = False
                    break
            else:
                fixed[r] = val

        if not ok:
            ans.append("0")
            continue

        free = 0
        for i in range(n):
            if find(i) == i and not zero[i] and i not in fixed:
                free += 1

        ans.append(str(pow(V % MOD, free, MOD)))

    print("\n".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
