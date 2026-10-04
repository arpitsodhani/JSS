# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []
for _ in range(t):
    n = data[idx]
    k = data[idx + 1]
    idx += 2
    p = data[idx:idx + n]
    idx += n
    bad = 0
    for i, x in enumerate(p, 1):
        if (i - x) % k != 0:
            bad += 1
    if bad == 0:
        ans.append('0')
    elif bad == 2:
        ans.append('1')
    else:
        ans.append('-1')
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
