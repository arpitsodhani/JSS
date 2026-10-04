import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        x = next(it)
        a = [0] + [next(it) for _ in range(n)]

        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = next(it)
            v = next(it)
            g[u].append(v)
            g[v].append(u)

        parent = [0] * (n + 1)
        parent[x] = -1
        order = [x]
        for u in order:
            for v in g[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)

        children = [[] for _ in range(n + 1)]
        for u in range(1, n + 1):
            if u != x:
                children[parent[u]].append(u)

        rev = order[::-1]
        size = [1] * (n + 1)
        sub_a = a[:]
        for u in rev:
            for v in children[u]:
                size[u] += size[v]
                sub_a[u] += sub_a[v]

        total = sub_a[x]

        prefs = []
        for r in range(n):
            cur = [0] * (n + 1)
            for u in rev:
                s = 1 if u <= r else 0
                for v in children[u]:
                    s += cur[v]
                cur[u] = s
            prefs.append(cur)

        need_dp = [0] * (n + 1)

        def ok(q, r):
            T = q * n + r
            if T < total or ((T - total) & 1):
                return False
            budget = (T - total) // 2
            pref = prefs[r]
            for u in rev:
                z = q * size[u] + pref[u] - sub_a[u]
                req = (z + 1) // 2 if z > 0 else 0
                s = 0
                for v in children[u]:
                    s += need_dp[v]
                need_dp[u] = req if req > s else s
            return need_dp[x] <= budget

        ans = None

        for r in range(n):
            if n % 2 == 0 and ((r - total) & 1):
                continue

            q0 = 0
            if total > r:
                q0 = (total - r + n - 1) // n

            step = 1
            if n % 2 == 1:
                p = (total - r) & 1
                if (q0 & 1) != p:
                    q0 += 1
                step = 2

            if ok(q0, r):
                q = q0
            else:
                hi = 1
                while not ok(q0 + step * hi, r):
                    hi <<= 1
                lo = 0
                while lo < hi:
                    mid = (lo + hi) // 2
                    if ok(q0 + step * mid, r):
                        hi = mid
                    else:
                        lo = mid + 1
                q = q0 + step * lo

            val = q * n + r
            if ans is None or val < ans:
                ans = val

        out.append(str(ans if ans is not None else -1))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
