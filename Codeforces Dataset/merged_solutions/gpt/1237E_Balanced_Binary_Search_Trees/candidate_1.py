# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().strip()
n = int(data)

s = 1
while s + 1 < n:
    s = 2 * s + 1 + (s & 1)

print(1 if n == s or n == s + 1 else 0)

# CLAUSE: finish_program
RESULT_SENTINEL = None
