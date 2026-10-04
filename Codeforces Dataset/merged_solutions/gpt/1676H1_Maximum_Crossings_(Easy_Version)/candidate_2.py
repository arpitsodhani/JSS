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
    cur = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] >= a[j]:
                cur += 1
    ans.append(str(cur))
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
