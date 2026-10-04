# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n, a = map(int, sys.stdin.readline().split())
best = 1
best_diff = abs(180 - a * n)
for t in range(2, n - 1):
    diff = abs(180 * t - a * n)
    if diff < best_diff:
        best_diff = diff
        best = t
print(2, 1, best + 2)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
