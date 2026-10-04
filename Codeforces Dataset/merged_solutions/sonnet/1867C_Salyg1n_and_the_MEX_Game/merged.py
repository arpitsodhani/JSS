# Clause setup_environment [Confidence: 0.40]
import sys

def next_missing(used, start):
    while used[start]:
        start += 1
    return start


# Clause solve_logic [Confidence: 0.80]
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


# Clause finish_program [Confidence: 0.80]



