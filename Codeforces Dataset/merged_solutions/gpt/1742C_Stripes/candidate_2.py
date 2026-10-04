# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
t = int(data[0])
idx = 1
ans = []
for _ in range(t):
    grid = data[idx:idx + 8]
    idx += 8
    found = False
    for row in grid:
        if row == 'R' * 8:
            ans.append('R')
            found = True
            break
    if not found:
        ans.append('B')
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
