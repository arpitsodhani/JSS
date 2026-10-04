# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, q = data[0], data[1]
a = data[2:2 + n]
queries = data[2 + n:2 + n + q]

d = deque(a)
mx = max(a)
before = []

while d[0] != mx:
    x = d.popleft()
    y = d.popleft()
    before.append((x, y))
    if x > y:
        d.appendleft(x)
        d.append(y)
    else:
        d.appendleft(y)
        d.append(x)

cycle = list(d)[1:]
k = len(before)

out = []
for m in queries:
    if m <= k:
        x, y = before[m - 1]
    else:
        x = mx
        y = cycle[(m - k - 1) % (n - 1)]
    out.append(f"{x} {y}")

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
