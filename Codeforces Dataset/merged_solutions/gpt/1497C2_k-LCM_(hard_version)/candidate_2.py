# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
out = []
idx = 1
for _ in range(t):
    n = data[idx]
    k = data[idx + 1]
    idx += 2
    ans = [1] * (k - 3)
    x = n - (k - 3)
    if x % 2 == 1:
        ans += [1, x // 2, x // 2]
    elif x % 4 == 0:
        ans += [x // 2, x // 4, x // 4]
    else:
        ans += [2, (x - 2) // 2, (x - 2) // 2]
    out.append(' '.join(map(str, ans)))
sys.stdout.write('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
