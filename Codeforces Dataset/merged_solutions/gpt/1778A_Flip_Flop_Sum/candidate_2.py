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
    s = sum(a)
    best = -4
    for i in range(n - 1):
        if a[i] == -1 and a[i + 1] == -1:
            best = 4
            break
        if a[i] != a[i + 1]:
            best = max(best, 0)
    ans.append(str(s + best))
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
