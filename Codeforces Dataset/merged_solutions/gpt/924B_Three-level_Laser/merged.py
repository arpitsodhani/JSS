# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n, u = data[0], data[1]
e = data[2:]

ans = -1.0
r = 0

for l in range(n):
    while r + 1 < n and e[r + 1] - e[l] <= u:
        r += 1
    if r - l >= 2:
        ans = max(ans, (e[r] - e[l + 1]) / (e[r] - e[l]))

print(ans if ans >= 0 else -1)

# CLAUSE: finish_program
RESULT_SENTINEL = None
