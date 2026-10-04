# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10 ** 9 + 7
n = int(sys.stdin.readline())
fact = 1
for i in range(1, n + 1):
    fact = fact * i % MOD
ans = (fact - pow(2, n - 1, MOD)) % MOD
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
