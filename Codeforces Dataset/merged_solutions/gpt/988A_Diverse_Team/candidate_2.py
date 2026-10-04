# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n, k = (data[0], data[1])
a = data[2:2 + n]
seen = set()
ans = []
for i, x in enumerate(a, 1):
    if x not in seen:
        seen.add(x)
        ans.append(i)
        if len(ans) == k:
            break
if len(ans) < k:
    print('NO')
else:
    print('YES')
    print(*ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
