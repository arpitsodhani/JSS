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
    ans.append(str(max(a) - min(a)))
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
