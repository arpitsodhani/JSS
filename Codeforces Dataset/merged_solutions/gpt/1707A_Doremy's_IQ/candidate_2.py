# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
out = []
for _ in range(t):
    n = data[idx]
    q = data[idx + 1]
    idx += 2
    a = data[idx:idx + n]
    idx += n
    ans = ['0'] * n
    cur = 0
    for i in range(n - 1, -1, -1):
        if a[i] <= cur:
            ans[i] = '1'
        elif cur < q:
            ans[i] = '1'
            cur += 1
    out.append(''.join(ans))
print('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
