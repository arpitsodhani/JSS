import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = next(it)
            v = next(it)
            g[u].append(v)
            g[v].append(u)

        parent = [0] * (n + 1)
        depth = [0] * (n + 1)
        children = [0] * (n + 1)

        stack = [n]
        parent[n] = -1
        order = []
        while stack:
            v = stack.pop()
            order.append(v)
            for to in g[v]:
                if to == parent[v]:
                    continue
                parent[to] = v
                depth[to] = depth[v] + 1
                children[v] += 1
                stack.append(to)

        leaves = [[], []]
        for v in range(1, n + 1):
            if children[v] == 0:
                leaves[depth[v] & 1].append(v)

        ans = []
        col = depth[1] & 1

        for _ in range(n - 1):
            if not leaves[col ^ 1]:
                ans.append((1, 0))
                col ^= 1

            v = leaves[col ^ 1].pop()
            ans.append((2, v))

            p = parent[v]
            children[p] -= 1
            if children[p] == 0:
                leaves[depth[p] & 1].append(p)

            ans.append((1, 0))
            col ^= 1

        out.append(str(len(ans)))
        for typ, v in ans:
            if typ == 1:
                out.append("1")
            else:
                out.append(f"2 {v}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
