# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
p, q, n = (data[0], data[1], data[2])
a = data[3:3 + n]
if n > 1 and a[-1] == 1:
    a.pop()
    a[-1] += 1
ok = True
m = len(a)
for i, x in enumerate(a):
    if q == 0 or p // q != x:
        ok = False
        break
    p %= q
    if i == m - 1:
        if p != 0:
            ok = False
    else:
        if p == 0:
            ok = False
            break
        p, q = (q, p)
print('YES' if ok else 'NO')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
