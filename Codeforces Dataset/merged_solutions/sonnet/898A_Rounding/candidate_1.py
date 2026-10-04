# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = int(input())

last = n % 10
if last <= 5:
    print(n - last)
else:
    print(n + (10 - last))

# CLAUSE: finish_program
RESULT_SENTINEL = None
