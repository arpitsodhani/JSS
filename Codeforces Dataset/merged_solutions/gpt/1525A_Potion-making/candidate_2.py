# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []
for k in data[1:1 + t]:
    ans.append(str(100 // gcd(k, 100)))
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
