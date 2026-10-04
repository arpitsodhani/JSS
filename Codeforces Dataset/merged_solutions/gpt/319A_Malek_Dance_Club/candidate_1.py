# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 1000000007

s = sys.stdin.readline().strip()
n = len(s)

ans = 0
pow4 = 1

for i in range(n - 1, -1, -1):
    if s[i] == '1':
        ans = (ans + pow(2, n - (n - 1 - i) - 1, MOD) * pow4) % MOD
    pow4 = (pow4 * 4) % MOD

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
