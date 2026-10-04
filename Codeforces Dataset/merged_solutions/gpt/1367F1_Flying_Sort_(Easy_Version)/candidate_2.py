# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []
for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n
    order = sorted(range(n), key=lambda i: a[i])
    best = 1
    cur = 1
    for i in range(1, n):
        if order[i - 1] < order[i]:
            cur += 1
        else:
            cur = 1
        if cur > best:
            best = cur
    ans.append(str(n - best))
sys.stdout.write('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
