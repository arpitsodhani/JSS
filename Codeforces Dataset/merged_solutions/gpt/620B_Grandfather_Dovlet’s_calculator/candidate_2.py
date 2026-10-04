# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
a, b = map(int, sys.stdin.read().split())
total = 0
for n in range(a, b + 1):
    for ch in str(n):
        total += segments[ord(ch) - 48]
print(total)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
