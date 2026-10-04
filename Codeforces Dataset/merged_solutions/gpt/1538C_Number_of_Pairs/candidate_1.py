# CLAUSE: setup_environment
import sys
from bisect import bisect_left, bisect_right

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    l = data[idx + 1]
    r = data[idx + 2]
    idx += 3
    a = data[idx:idx + n]
    idx += n

    a.sort()
    res = 0

    for i in range(n):
        left = bisect_left(a, l - a[i], i + 1, n)
        right = bisect_right(a, r - a[i], i + 1, n)
        res += right - left

    ans.append(str(res))

sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
