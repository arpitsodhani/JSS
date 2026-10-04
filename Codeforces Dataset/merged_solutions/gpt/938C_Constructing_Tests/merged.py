# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
x = int(sys.stdin.readline())

for k in range(1, 1000000):
    n2 = x + k * k
    n = math.isqrt(n2)
    if n * n == n2 and n // k >= 2:
        print(n, n // k)
        break
else:
    print(-1)

# CLAUSE: finish_program
RESULT_SENTINEL = None
