# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
s = sys.stdin.read().split()

if len(s) >= 2:
    a, b = s[0], s[1]
else:
    t = s[0]
    m = len(t) // 2
    a, b = t[:m], t[m:]

x = y = 0

for ca, cb in zip(a, b):
    if ca != cb:
        if ca == '4':
            x += 1
        else:
            y += 1

print(max(x, y))

# CLAUSE: finish_program
RESULT_SENTINEL = None
