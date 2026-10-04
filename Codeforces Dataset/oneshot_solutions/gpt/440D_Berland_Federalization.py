import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, k = data[0], data[1]
    g = [[] for _ in range(n + 1)]

    p = 2
    for idx in range(1, n):
        a, b = data[p], data[p + 1]
        p += 2
        g[a].append((b, idx))
        g[b].append((a, idx))

    parent = [0] * (n + 1)
    pedge = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    order = [1]
    parent[1] = -1

    for u in order:
        for v, eid in g[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            pedge[v] = eid
            children[u].append((v, eid))
            order.append(v)

    inf = 10 ** 9
    dp = [[inf] * (k + 1) for _ in range(n + 1)]
    sz = [0] * (n + 1)
    choice = [[] for _ in range(n + 1)]

    for u in reversed(order):
        dp[u][1] = 0
        sz[u] = 1

        for v, eid in children[u]:
            ndp = [inf] * (k + 1)
            take = [-1] * (k + 1)

            for cur in range(1, min(sz[u], k) + 1):
                if dp[u][cur] >= inf:
                    continue

                val = dp[u][cur] + 1
                if val < ndp[cur]:
                    ndp[cur] = val
                    take[cur] = 0

                lim = min(sz[v], k - cur)
                for add in range(1, lim + 1):
                    val = dp[u][cur] + dp[v][add]
                    if val < ndp[cur + add]:
                        ndp[cur + add] = val
                        take[cur + add] = add

            dp[u] = ndp
            choice[u].append(take)
            sz[u] = min(k, sz[u] + sz[v])

    best = inf
    root = 1
    for u in range(1, n + 1):
        val = dp[u][k] + (0 if u == 1 else 1)
        if val < best:
            best = val
            root = u

    ans = []

    def restore(u, need):
        for i in range(len(children[u]) - 1, -1, -1):
            v, eid = children[u][i]
            t = choice[u][i][need]
            if t == 0:
                ans.append(eid)
            else:
                restore(v, t)
                need -= t

    restore(root, k)
    if root != 1:
        ans.append(pedge[root])

    out = [str(len(ans))]
    if ans:
        out.append(" ".join(map(str, ans)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
