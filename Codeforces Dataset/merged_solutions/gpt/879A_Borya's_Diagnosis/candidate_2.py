# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pos = 1
    day = 0
    for _ in range(n):
        s = data[pos]
        d = data[pos + 1]
        pos += 2
        if s > day:
            day = s
        else:
            day = s + ((day - s) // d + 1) * d
    print(day)
solve()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
