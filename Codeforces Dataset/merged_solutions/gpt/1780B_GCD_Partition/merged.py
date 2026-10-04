# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n

    total = sum(a)
    pref = 0
    best = 0

    for i in range(n - 1):
        pref += a[i]
        best = max(best, gcd(pref, total))

    ans.append(str(best))

print("\n".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
