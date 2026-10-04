# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
t = data[1:1 + n]

active = {0}
ans = 1

for i, x in enumerate(t, 1):
    if x in active:
        active.remove(x)
    else:
        ans += 1
    active.add(i)

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
