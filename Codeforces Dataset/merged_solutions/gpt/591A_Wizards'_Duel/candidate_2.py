# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(float, sys.stdin.read().split()))
l, p, q = data
print(l * p / (p + q))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
