# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
if len(data) >= 2:
    n = int(data[0])
    x = int(data[1])
else:
    s = data[0]
    n = int(s[:-1])
    x = int(s[-1])

for i in range(n % 6, 0, -1):
    move = n - (n % 6) + i
    if move % 2 == 1:
        if x == 0:
            x = 1
        elif x == 1:
            x = 0
    else:
        if x == 1:
            x = 2
        elif x == 2:
            x = 1

print(x)

# CLAUSE: finish_program
RESULT_SENTINEL = None
