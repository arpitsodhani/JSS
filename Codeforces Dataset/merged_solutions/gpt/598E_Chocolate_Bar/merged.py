# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
INF = 10 ** 9
MAX_N = 30
MAX_K = 50

dp = [[[INF] * (MAX_K + 1) for _ in range(MAX_N + 1)] for __ in range(MAX_N + 1)]

for n in range(1, MAX_N + 1):
    for m in range(1, MAX_N + 1):
        dp[n][m][0] = 0
        if n * m <= MAX_K:
            dp[n][m][n * m] = 0

for n in range(1, MAX_N + 1):
    for m in range(1, MAX_N + 1):
        limit = min(MAX_K, n * m)
        for k in range(1, limit + 1):
            if k == n * m:
                continue
            best = dp[n][m][k]
            for cut in range(1, n):
                cost = m * m
                for x in range(k + 1):
                    if x <= cut * m and k - x <= (n - cut) * m:
                        val = dp[cut][m][x] + dp[n - cut][m][k - x] + cost
                        if val < best:
                            best = val
            for cut in range(1, m):
                cost = n * n
                for x in range(k + 1):
                    if x <= n * cut and k - x <= n * (m - cut):
                        val = dp[n][cut][x] + dp[n][m - cut][k - x] + cost
                        if val < best:
                            best = val
            dp[n][m][k] = best

data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []
idx = 1

for _ in range(t):
    n, m, k = data[idx], data[idx + 1], data[idx + 2]
    idx += 3
    ans.append(str(dp[n][m][k]))

sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
