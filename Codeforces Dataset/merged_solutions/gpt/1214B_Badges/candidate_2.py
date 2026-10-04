# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
b = int(input())
g = int(input())
n = int(input())
lo = max(0, n - g)
hi = min(b, n)
print(max(0, hi - lo + 1))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
