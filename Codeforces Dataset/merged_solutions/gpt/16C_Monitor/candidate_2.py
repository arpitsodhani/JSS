# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
a, b, x, y = map(int, sys.stdin.read().split())
g = gcd(x, y)
x //= g
y //= g
k = min(a // x, b // y)
print(x * k, y * k)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
