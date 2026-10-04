# CLAUSE: setup_environment
import sys
from math import atan2, acos, hypot, pi

tokens = list(map(int, sys.stdin.buffer.read().split()))
n, k = tokens[0], tokens[1]
origin_hits = 0
polar = []
for idx in range(2, len(tokens), 2):
    x = tokens[idx]
    y = tokens[idx + 1]
    if x == 0 and y == 0:
        origin_hits += 1
    else:
        polar.append((hypot(x, y), atan2(y, x)))

full = 2.0 * pi

# CLAUSE: solve_logic
def enough(r):
    need = k - origin_hits
    if need <= 0:
        return True
    if r == 0.0:
        return False
    starts = []
    ends = []
    diameter = r + r + 1e-11
    for d, a in polar:
        if d > diameter:
            continue
        w = acos(min(1.0, d / (r + r)))
        left = (a - w) % full
        right = (a + w) % full
        if left <= right:
            starts.append(left)
            ends.append(right)
        else:
            starts.append(left)
            ends.append(full)
            starts.append(0.0)
            ends.append(right)
    starts.sort()
    ends.sort()
    i = 0
    j = 0
    active = 0
    while i < len(starts):
        if j == len(ends) or starts[i] <= ends[j] + 1e-15:
            active += 1
            if active >= need:
                return True
            i += 1
        else:
            active -= 1
            j += 1
    return False

low = 0.0
high = 200000.0
iteration = 0
while iteration < 100:
    middle = (low + high) / 2.0
    if enough(middle):
        high = middle
    else:
        low = middle
    iteration += 1

# CLAUSE: finish_program
sys.stdout.write("{:.10f}\n".format(high))
