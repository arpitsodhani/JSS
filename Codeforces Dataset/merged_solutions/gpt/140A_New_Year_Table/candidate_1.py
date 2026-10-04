# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
n, R, r = map(int, sys.stdin.read().split())

if n == 1:
    print("YES" if r <= R else "NO")
else:
    print("YES" if R >= 2 * r and (R - r) * math.sin(math.pi / n) + 1e-12 >= r else "NO")

# CLAUSE: finish_program
RESULT_SENTINEL = None
