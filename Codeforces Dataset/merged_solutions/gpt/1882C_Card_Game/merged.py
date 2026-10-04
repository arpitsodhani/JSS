# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n

    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + (a[i] if a[i] > 0 else 0)

    ans = 0
    for i in range(n):
        cur = suffix[i + 1]
        if i % 2 == 0:
            cur += a[i]
        if cur > ans:
            ans = cur

    out.append(str(ans))

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
