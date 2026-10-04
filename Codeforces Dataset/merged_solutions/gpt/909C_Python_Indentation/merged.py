# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10**9 + 7

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
a = ''.join(data[1:])[:n]

dp = [0] * (n + 2)
dp[0] = 1

for i in range(1, n):
    ndp = [0] * (n + 2)
    if a[i - 1] == 'f':
        for j in range(n):
            ndp[j + 1] = dp[j]
    else:
        run = 0
        for j in range(n, -1, -1):
            run = (run + dp[j]) % MOD
            ndp[j] = run
    dp = ndp

print(sum(dp) % MOD)

# CLAUSE: finish_program
RESULT_SENTINEL = None
