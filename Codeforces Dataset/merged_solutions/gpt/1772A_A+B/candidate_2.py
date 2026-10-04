# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
t = int(data[0])
ans = []
for i in range(1, t + 1):
    a, b = data[i].split('+')
    ans.append(str(int(a) + int(b)))
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
