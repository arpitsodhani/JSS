import sys
from bisect import bisect_left

def tri(v):
    return v * (v + 1) // 2

n, x = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))
a = d * 2

pd = [0]
ph = [0]
for v in a:
    pd.append(pd[-1] + v)
    ph.append(ph[-1] + tri(v))

ans = 0
for r in range(1, 2 * n + 1):
    target = pd[r] - x
    l = bisect_left(pd, target, 0, r + 1)
    cur = ph[r] - ph[l]
    used = pd[r] - pd[l]
    rem = x - used
    if rem > 0 and l > 0:
        v = a[l - 1]
        cur += tri(v) - tri(v - rem)
    ans = max(ans, cur)

print(ans)
