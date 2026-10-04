# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10**9 + 7

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
x = sorted(data[1:])

pow2 = [1] * n
for i in range(1, n):
    pow2[i] = (pow2[i - 1] * 2) % MOD

ans = 0
for i, v in enumerate(x):
    ans = (ans + v * (pow2[i] - pow2[n - 1 - i])) % MOD

print(ans % MOD)

# CLAUSE: finish_program
RESULT_SENTINEL = None
