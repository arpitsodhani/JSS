# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
ans = []
for _ in range(t):
    n, H, M = (data[idx], data[idx + 1], data[idx + 2])
    idx += 3
    current = H * 60 + M
    best = 24 * 60
    for _ in range(n):
        h, m = (data[idx], data[idx + 1])
        idx += 2
        alarm = h * 60 + m
        diff = (alarm - current) % (24 * 60)
        best = min(best, diff)
    ans.append(f'{best // 60} {best % 60}')
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
