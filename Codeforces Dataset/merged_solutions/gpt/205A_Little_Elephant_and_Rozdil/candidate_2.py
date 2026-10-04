# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:1 + n]
mn = min(a)
if a.count(mn) == 1:
    print(a.index(mn) + 1)
else:
    print('Still Rozdil')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
