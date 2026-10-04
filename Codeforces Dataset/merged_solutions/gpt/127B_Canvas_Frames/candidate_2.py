# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()
n = data[0]
sticks = data[1:1 + n]
pairs = sum((count // 2 for count in Counter(sticks).values()))
print(pairs // 2)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
