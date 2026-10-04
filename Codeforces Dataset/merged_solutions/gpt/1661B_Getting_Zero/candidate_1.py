# CLAUSE: setup_environment
from collections import deque
import sys

# CLAUSE: solve_logic
MOD = 32768

dist = [-1] * MOD
dist[0] = 0
q = deque([0])

while q:
    x = q.popleft()
    for y in ((x - 1) % MOD, x // 2 if x % 2 == 0 else -1, x // 2 + MOD // 2 if x % 2 == 0 else -1):
        if y != -1 and dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:1 + n]

print(*[dist[x] for x in a])

# CLAUSE: finish_program
RESULT_SENTINEL = None
