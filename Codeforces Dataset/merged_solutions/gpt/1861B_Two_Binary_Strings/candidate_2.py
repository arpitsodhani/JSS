# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
t = int(data[0])
idx = 1
ans = []
for _ in range(t):
    a = data[idx]
    b = data[idx + 1]
    idx += 2
    ok = False
    for i in range(len(a) - 1):
        if a[i] == b[i] == '0' and a[i + 1] == b[i + 1] == '1':
            ok = True
            break
    ans.append('YES' if ok else 'NO')
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
