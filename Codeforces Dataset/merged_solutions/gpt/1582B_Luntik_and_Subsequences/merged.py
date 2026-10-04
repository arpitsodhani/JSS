# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    out = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        arr = data[pos:pos + n]
        pos += n
        out.append(str(arr.count(1) * (1 << arr.count(0))))
    print("\n".join(out))

solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
