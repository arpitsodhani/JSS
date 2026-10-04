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
    a = data[idx:idx + n]
    idx += n
    mx = max(a)
    mn = min(a)
    s = sum(a)
    cnt_mx = a.count(mx)
    if mx - mn > k + 1:
        ans.append('Jerry')
    elif mx - mn == k + 1 and cnt_mx > 1:
        ans.append('Jerry')
    else:
        ans.append('Tom' if s % 2 else 'Jerry')
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
