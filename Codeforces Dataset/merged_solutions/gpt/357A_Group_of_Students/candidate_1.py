# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
a = list(map(int, sys.stdin.read().split()))
m = a[0]
c = a[1:1 + m]
x, y = a[1 + m], a[2 + m]

total = sum(c)
beginners = 0

for k in range(1, m + 1):
    intermediate = total - beginners
    if x <= beginners <= y and x <= intermediate <= y:
        print(k)
        break
    beginners += c[k - 1]
else:
    print(0)

# CLAUSE: finish_program
RESULT_SENTINEL = None
