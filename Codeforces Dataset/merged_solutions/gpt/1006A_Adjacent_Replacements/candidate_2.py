# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:1 + n]
print(*[x - 1 if x % 2 == 0 else x for x in a])

# CLAUSE: finish_program
RESULT_SENTINEL = 0
