# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)

    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        deg[u] += 1
        deg[v] += 1
        if u < v:
            adj[u].append(v)
        else:
            adj[v].append(u)

    dp = [1] * (n + 1)

    for u in range(1, n + 1):
        nd = dp[u] + 1
        for v in adj[u]:
            if dp[v] < nd:
                dp[v] = nd

    ans = 0
    for i in range(1, n + 1):
        val = dp[i] * deg[i]
        if val > ans:
            ans = val

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
