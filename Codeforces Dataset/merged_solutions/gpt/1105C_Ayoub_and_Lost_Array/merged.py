# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10 ** 9 + 7

n, l, r = map(int, sys.stdin.readline().split())

def upto(x):
    q, m = divmod(x, 3)
    return [q, q + (m >= 1), q + (m >= 2)]

a = upto(r)
b = upto(l - 1)
cnt = [(a[i] - b[i]) % MOD for i in range(3)]

dp0, dp1, dp2 = 1, 0, 0

for _ in range(n):
    ndp0 = (dp0 * cnt[0] + dp1 * cnt[2] + dp2 * cnt[1]) % MOD
    ndp1 = (dp0 * cnt[1] + dp1 * cnt[0] + dp2 * cnt[2]) % MOD
    ndp2 = (dp0 * cnt[2] + dp1 * cnt[1] + dp2 * cnt[0]) % MOD
    dp0, dp1, dp2 = ndp0, ndp1, ndp2

print(dp0)

# CLAUSE: finish_program
RESULT_SENTINEL = None
