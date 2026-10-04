# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
data = sys.stdin.read().split()
if not data:
    sys.exit()
n = int(data[0])
seqs = data[1:]
pos = defaultdict(int)
neg = defaultdict(int)
for s in seqs:
    bal = 0
    mn = 0
    for c in s:
        if c == '(':
            bal += 1
        else:
            bal -= 1
        if bal < mn:
            mn = bal
    if bal >= 0:
        if mn >= 0:
            pos[bal] += 1
    elif mn >= bal:
        neg[-bal] += 1
ans = pos[0] * pos[0]
for k, v in pos.items():
    if k:
        ans += v * neg[k]
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
