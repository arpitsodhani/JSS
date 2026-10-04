# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().strip().split()
q = int(data[0])
idx = 1
out = []
for _ in range(q):
    n = int(data[idx])
    s = data[idx + 1]
    idx += 2
    if n == 2 and s[0] >= s[1]:
        out.append('NO')
    else:
        out.append('YES')
        out.append('2')
        out.append(f'{s[0]} {s[1:]}')
print('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
