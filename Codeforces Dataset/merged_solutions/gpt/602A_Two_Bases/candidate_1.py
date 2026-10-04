# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
p = 0

n = data[p]
bx = data[p + 1]
p += 2
x_digits = data[p:p + n]
p += n

m = data[p]
by = data[p + 1]
p += 2
y_digits = data[p:p + m]

x = 0
for d in x_digits:
    x = x * bx + d

y = 0
for d in y_digits:
    y = y * by + d

if x < y:
    print("<")
elif x > y:
    print(">")
else:
    print("=")

# CLAUSE: finish_program
RESULT_SENTINEL = None
