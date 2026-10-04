# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[:2]
    prices = sorted(data[2:2 + n])
    ans = 0
    for x in prices[:m]:
        if x < 0:
            ans -= x
    print(ans)

solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
