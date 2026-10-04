# CLAUSE: setup_environment
from itertools import combinations
import sys

# CLAUSE: solve_logic
a = list(map(int, sys.stdin.read().split()))
total = sum(a)
ok = False
for comb in combinations(range(6), 3):
    if sum((a[i] for i in comb)) * 2 == total:
        ok = True
        break
print('YES' if ok else 'NO')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
