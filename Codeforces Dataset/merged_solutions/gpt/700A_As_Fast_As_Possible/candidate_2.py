# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
n, l, v1, v2, k = map(int, sys.stdin.readline().split())
groups = (n + k - 1) // k
if groups == 1:
    print('{:.10f}'.format(l / v2))
else:
    q = groups
    coef = (v2 - v1) / (v2 + v1)
    low, high = (0.0, l / v1)
    for _ in range(100):
        mid = (low + high) / 2.0
        ride = (l - v1 * mid) / (v2 - v1)
        cycle = ride * (1.0 + coef)
        last_start = (q - 1) * cycle
        last_pos = v1 * last_start
        last_finish = last_start + (l - last_pos) / v2
        if last_finish <= mid:
            high = mid
        else:
            low = mid
    print('{:.10f}'.format(high))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
