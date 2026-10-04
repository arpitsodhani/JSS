# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
a = data[1:1 + n]

inf = 10 ** 9
ans = [inf] * n

last = -inf
for i in range(n):
    if a[i] == 0:
        last = i
    ans[i] = i - last

last = inf
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        last = i
    ans[i] = min(ans[i], last - i)

print(*ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
