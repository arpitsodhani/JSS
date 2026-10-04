# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
n = int(sys.stdin.readline())
r = math.isqrt(n)
ans = -1
for x in range(max(1, r - 200), r + 1):
    if x * x + sum(map(int, str(x))) * x == n:
        ans = x
        break
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
