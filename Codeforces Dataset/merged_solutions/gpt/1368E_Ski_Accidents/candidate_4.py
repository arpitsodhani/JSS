# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2

        g = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = data[idx]
            v = data[idx + 1]
            idx += 2
            g[u].append(v)

        dp = [0] * (n + 1)
        closed = [False] * (n + 1)
        ans = []

        for u in range(1, n + 1):
            if closed[u]:
                continue
            for v in g[u]:
                if not closed[v]:
                    if dp[v] < dp[u] + 1:
                        dp[v] = dp[u] + 1
                    if dp[v] == 2:
                        closed[v] = True
                        ans.append(v)

        out.append(str(len(ans)))
        out.append(" ".join(map(str, ans)))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
