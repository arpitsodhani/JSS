# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()
n, b = (data[0], data[1])
q = deque()
ans = []
idx = 2
for _ in range(n):
    t = data[idx]
    d = data[idx + 1]
    idx += 2
    while q and q[0] <= t:
        q.popleft()
    if len(q) <= b:
        start = t if not q else q[-1]
        finish = start + d
        q.append(finish)
        ans.append(finish)
    else:
        ans.append(-1)
print(*ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
