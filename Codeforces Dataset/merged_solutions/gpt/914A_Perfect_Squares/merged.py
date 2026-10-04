# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:1 + n]

ans = -10**18
for x in a:
    if x < 0:
        ans = max(ans, x)
    else:
        r = math.isqrt(x)
        if r * r != x:
            ans = max(ans, x)

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
