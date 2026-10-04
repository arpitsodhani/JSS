# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
ans = []
for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n
    ok = True
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) not in (5, 7):
            ok = False
            break
    ans.append('YES' if ok else 'NO')
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
