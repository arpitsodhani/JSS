# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []
idx = 1
for _ in range(t):
    a, b, c = (data[idx], data[idx + 1], data[idx + 2])
    idx += 3
    first = abs(a - 1)
    second = abs(b - c) + abs(c - 1)
    if first < second:
        ans.append('1')
    elif second < first:
        ans.append('2')
    else:
        ans.append('3')
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
