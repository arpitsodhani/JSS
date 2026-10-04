# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def good(n, k):
    return n - math.isqrt(n) >= k

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
ans = []

for k in data[1:1 + t]:
    l, r = 1, 2 * k + 10
    while l < r:
        m = (l + r) // 2
        if good(m, k):
            r = m
        else:
            l = m + 1
    ans.append(str(l))

print("\n".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
