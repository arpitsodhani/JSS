# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
out = []
for i in range(1, t + 1):
    n = data[i]
    if n == 1:
        out.append('1')
    elif n == 2:
        out.append('-1')
    else:
        nums = list(range(1, n * n + 1, 2)) + list(range(2, n * n + 1, 2))
        for r in range(n):
            out.append(' '.join(map(str, nums[r * n:(r + 1) * n])))
sys.stdout.write('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
