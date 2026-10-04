# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
out = []
for _ in range(t):
    n = data[idx]
    x = data[idx + 1]
    idx += 2
    if x == 0:
        p = list(range(1, n)) + [0]
    elif x == n:
        p = list(range(n))
    else:
        p = list(range(x)) + list(range(x + 1, n)) + [x]
    out.append(' '.join(map(str, p)))
print('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
