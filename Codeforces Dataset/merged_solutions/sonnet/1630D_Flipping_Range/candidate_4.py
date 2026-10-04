# CLAUSE: setup_environment
import sys
from math import gcd
from functools import reduce

# CLAUSE: solve_logic
def compute(values, lengths):
    g = reduce(gcd, lengths)
    minimum = [None] * g
    negative_count = [0] * g
    total = 0

    for i, x in enumerate(values):
        y = abs(x)
        total += y
        r = i % g
        if x < 0:
            negative_count[r] += 1
        if minimum[r] is None or y < minimum[r]:
            minimum[r] = y

    losses = [0, 0]
    for r in range(g):
        losses[negative_count[r] & 1] += 2 * minimum[r]

    a = total - losses[1]
    b = total - losses[0]
    return max(a, b)

# CLAUSE: finish_program
def main():
    raw = sys.stdin.buffer.read().split()
    it = iter(raw)
    t = int(next(it))
    res = []
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        values = [int(next(it)) for _ in range(n)]
        lengths = [int(next(it)) for _ in range(m)]
        res.append(str(compute(values, lengths)))
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
