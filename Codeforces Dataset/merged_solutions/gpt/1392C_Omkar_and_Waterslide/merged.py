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

    res = 0
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            res += a[i] - a[i + 1]
    ans.append(str(res))

print("\n".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
