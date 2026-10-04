# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
a, b, x, y = map(int, sys.stdin.readline().split())
g = gcd(x, y)
x //= g
y //= g
print(min(a // x, b // y))

# CLAUSE: finish_program
RESULT_SENTINEL = None
