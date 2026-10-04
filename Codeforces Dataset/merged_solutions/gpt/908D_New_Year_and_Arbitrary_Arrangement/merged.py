# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10**9 + 7

k, pa, pb = map(int, input().split())

inv_sum = pow(pa + pb, MOD - 2, MOD)
a = pa * inv_sum % MOD
b = pb * inv_sum % MOD
inv_b = pow(b, MOD - 2, MOD)

dp = [[0] * k for _ in range(k)]
dp[1][0] = a * pow(b, MOD - 2, MOD) % MOD

ans = 0

for i in range(1, k):
    for j in range(k):
        cur = dp[i][j]
        if cur == 0:
            continue

        if i + 1 == k:
            ans = (ans + cur * a % MOD * (j + k + a * inv_b % MOD)) % MOD
        else:
            dp[i + 1][j] = (dp[i + 1][j] + cur * a) % MOD

        nj = j + i
        if nj >= k:
            ans = (ans + cur * b % MOD * nj) % MOD
        else:
            dp[i][nj] = (dp[i][nj] + cur * b) % MOD

print(ans % MOD)

# CLAUSE: finish_program
RESULT_SENTINEL = None
