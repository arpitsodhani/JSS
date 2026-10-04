# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
if not data:
    sys.exit()
n = int(data[0])
pos = 0
ok = True
idx = 1
for _ in range(n):
    t = int(data[idx])
    d = data[idx + 1]
    idx += 2
    if pos == 0:
        if d != 'South':
            ok = False
            break
    elif pos == 20000:
        if d != 'North':
            ok = False
            break
    if d == 'South':
        pos += t
    elif d == 'North':
        pos -= t
    if pos < 0 or pos > 20000:
        ok = False
        break
print('YES' if ok and pos == 0 else 'NO')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
