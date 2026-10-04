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
        arr = sorted(data[pos:pos + n], reverse=True)
        pos += n
        second = arr[1] if n > 1 else 0
        out.append('YES' if arr[0] <= second + 1 else 'NO')
    print('\n'.join(out))
solve()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
