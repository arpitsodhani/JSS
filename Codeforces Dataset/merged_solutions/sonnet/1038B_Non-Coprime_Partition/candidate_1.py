# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = int(input())

if n <= 2:
    print("No")
else:
    print("Yes")
    print(1, n)
    print(n - 1, *range(1, n))

# CLAUSE: finish_program
RESULT_SENTINEL = None
