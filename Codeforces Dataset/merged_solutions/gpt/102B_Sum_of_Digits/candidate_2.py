# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = sys.stdin.readline().strip()
count = 0
while len(n) > 1:
    n = str(sum((int(c) for c in n)))
    count += 1
print(count)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
