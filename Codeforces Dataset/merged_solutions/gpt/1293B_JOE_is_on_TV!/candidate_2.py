# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = int(sys.stdin.readline())
ans = sum((1.0 / i for i in range(1, n + 1)))
print(f'{ans:.12f}')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
