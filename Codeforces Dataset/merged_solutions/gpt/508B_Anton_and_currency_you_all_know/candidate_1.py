# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
s = list(input().strip())
last = int(s[-1])
pos = -1

for i in range(len(s) - 1):
    d = int(s[i])
    if d % 2 == 0:
        pos = i
        if d < last:
            break

if pos == -1:
    print(-1)
else:
    s[pos], s[-1] = s[-1], s[pos]
    print(''.join(s))

# CLAUSE: finish_program
RESULT_SENTINEL = None
