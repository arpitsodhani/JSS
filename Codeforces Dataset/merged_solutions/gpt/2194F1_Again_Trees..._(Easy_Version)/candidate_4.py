# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    MOD = 10**9 + 7

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        p = 0
        t = data[p]
        p += 1
        out = []

        for _ in range(t):
            n = data[p]
            k = data[p + 1]
            p += 2

            adj = [[] for _ in range(n)]
            for _ in range(n - 1):
                u = data[p] - 1
                v = data[p + 1] - 1
                p += 2
                adj[u].append(v)
                adj[v].append(u)

            a = data[p:p + n]
            p += n
            b = data[p:p + k]
            p += k

            parent = [-2] * n
            parent[0] = -1
            order = [0]

            for v in order:
                for to in adj[v]:
                    if to != parent[v]:
                        parent[to] = v
                        order.append(to)

            dp = [None] * n

            for v in reversed(order):
                cur = {a[v]: 1}

                for to in adj[v]:
                    if parent[to] != v:
                        continue

                    child = dp[to]
                    dp[to] = None

                    cut = 0
                    for x in b:
                        cut += child.get(x, 0)
                    cut %= MOD

                    nxt = {}

                    if cut:
                        for x, cx in cur.items():
                            nxt[x] = (nxt.get(x, 0) + cx * cut) % MOD

                    for x, cx in cur.items():
                        for y, cy in child.items():
                            z = x ^ y
                            nxt[z] = (nxt.get(z, 0) + cx * cy) % MOD

                    cur = nxt

                dp[v] = cur

            ans = 0
            for x in b:
                ans += dp[0].get(x, 0)

            out.append(str(ans % MOD))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
