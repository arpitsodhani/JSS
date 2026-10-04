# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = int(sys.stdin.readline())
ans = 10 ** 30
p = 1
while p <= n * 10:
    for d in range(1, 10):
        x = d * p
        if x > n:
            ans = min(ans, x - n)
    p *= 10
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
