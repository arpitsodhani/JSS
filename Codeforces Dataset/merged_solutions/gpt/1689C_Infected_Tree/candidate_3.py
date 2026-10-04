# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            idx += 1

            g = [[] for _ in range(n + 1)]
            for _ in range(n - 1):
                u = data[idx]
                v = data[idx + 1]
                idx += 2
                g[u].append(v)
                g[v].append(u)

            parent = [0] * (n + 1)
            order = [1]
            parent[1] = -1

            for u in order:
                for v in g[u]:
                    if v != parent[u]:
                        parent[v] = u
                        order.append(v)

            size = [1] * (n + 1)
            dp = [0] * (n + 1)

            for u in reversed(order):
                children = []
                total = 1

                for v in g[u]:
                    if parent[v] == u:
                        children.append(v)
                        total += size[v]

                size[u] = total

                if len(children) == 1:
                    a = children[0]
                    dp[u] = size[a] - 1
                elif len(children) == 2:
                    a, b = children
                    dp[u] = max(size[a] - 1 + dp[b], size[b] - 1 + dp[a])

            out.append(str(dp[1]))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
