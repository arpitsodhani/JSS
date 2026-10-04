# CLAUSE: setup_environment
import sys
from bisect import bisect_left, bisect_right

# CLAUSE: solve_logic
MOD = 1000000007

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
buses = []
coords = [0, n]

p = 2
for _ in range(m):
    s, t = data[p], data[p + 1]
    p += 2
    buses.append((t, s))
    coords.append(s)
    coords.append(t)

coords = sorted(set(coords))
idx = {x: i + 1 for i, x in enumerate(coords)}
size = len(coords) + 2

bit = [0] * (size + 1)

def add(i, v):
    while i <= size:
        bit[i] = (bit[i] + v) % MOD
        i += i & -i

def pref(i):
    res = 0
    while i > 0:
        res = (res + bit[i]) % MOD
        i -= i & -i
    return res

def range_sum(l, r):
    if l > r:
        return 0
    return (pref(r) - pref(l - 1)) % MOD

add(idx[0], 1)
buses.sort()

for t, s in buses:
    l = bisect_left(coords, s) + 1
    r = bisect_left(coords, t) + 1 - 1
    ways = range_sum(l, r)
    if ways:
        add(idx[t], ways)

print(range_sum(idx[n], idx[n]) % MOD)

# CLAUSE: finish_program
RESULT_SENTINEL = None
