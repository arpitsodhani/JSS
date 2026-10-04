# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = int(sys.stdin.readline())
ans = list(range(2, n + 1)) + [1]
print(*ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
