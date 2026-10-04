# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
v = list(map(int, sys.stdin.read().split()))
a1, b1, a2, b2, a3, b3 = v
ok = False
for x2, y2 in ((a2, b2), (b2, a2)):
    for x3, y3 in ((a3, b3), (b3, a3)):
        if max(x2, x3) <= a1 and y2 + y3 <= b1:
            ok = True
        if x2 + x3 <= a1 and max(y2, y3) <= b1:
            ok = True
print('YES' if ok else 'NO')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
