# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
a, b, c, d, e, f = map(int, sys.stdin.read().split())
if b * d * f > a * c * e:
    print('Ron')
else:
    print('Hermione')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
