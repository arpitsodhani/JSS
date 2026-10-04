# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n, p1, p2, p3, t1, t2 = data[:6]

intervals = []
idx = 6
for _ in range(n):
    intervals.append((data[idx], data[idx + 1]))
    idx += 2

ans = 0

for i, (l, r) in enumerate(intervals):
    ans += (r - l) * p1

    if i + 1 < n:
        gap = intervals[i + 1][0] - r

        a = min(gap, t1)
        ans += a * p1
        gap -= a

        b = min(gap, t2)
        ans += b * p2
        gap -= b

        ans += gap * p3

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
