# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()
n = data[0]
a = data[1:1 + n]
ans = 0
for i in range(n):
    cur = 0
    for j in range(i, n):
        cur ^= a[j]
        if cur > ans:
            ans = cur
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
