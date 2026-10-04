# CLAUSE: setup_environment
import sys

def mex(values):
    x = 0
    while x in values:
        x += 1
    return x

# CLAUSE: solve_logic
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = set(map(int, sys.stdin.readline().split()))
    while True:
        x = mex(s)
        print(x, flush=True)
        s.add(x)
        y = int(sys.stdin.readline())
        if y == -1:
            break
        s.discard(y)

# CLAUSE: finish_program
