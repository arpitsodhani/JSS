# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
a, b = map(int, input().split())

while a and b:
    if a >= 2 * b:
        a %= 2 * b
    elif b >= 2 * a:
        b %= 2 * a
    else:
        break

print(a, b)

# CLAUSE: finish_program
RESULT_SENTINEL = None
