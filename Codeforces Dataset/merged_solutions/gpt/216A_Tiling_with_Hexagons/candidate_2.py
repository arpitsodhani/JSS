# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
a, b, c = map(int, sys.stdin.read().split())
print(a * b + b * c + c * a - a - b - c + 1)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
