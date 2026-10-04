# CLAUSE: setup_environment
import sys
from itertools import accumulate

# CLAUSE: solve_logic
def solve():
    raw = sys.stdin.buffer.read().split()
    k = 0
    tests = int(raw[k])
    k += 1
    out = []
    for _ in range(tests):
        n = int(raw[k])
        k += 1
        arr = [int(x) for x in raw[k:k + n]]
        k += n
        prefix = list(accumulate(arr, initial=0))
        low = prefix[0]
        best = -10**30
        for value in prefix[1:]:
            candidate = value - low
            if candidate > best:
                best = candidate
            if value < low:
                low = value
        out.append(str(best))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
solve()
