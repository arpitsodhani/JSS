import sys
from math import gcd, log2

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
a = data[1:]

lg = [0] * (n + 1)
for i in range(2, n + 1):
    lg[i] = lg[i // 2] + 1

st = [a]
k = 1
while (1 << k) <= n:
    prev = st[-1]
    length = 1 << k
    half = length >> 1
    row = [0] * (n - length + 1)
    for i in range(n - length + 1):
        row[i] = gcd(prev[i], prev[i + half])
    st.append(row)
    k += 1

def get_gcd(l, r):
    p = lg[r - l + 1]
    return gcd(st[p][l], st[p][r - (1 << p) + 1])

best = -1
starts = []

for i, x in enumerate(a):
    lo, hi = 0, i
    left = i
    while lo <= hi:
        mid = (lo + hi) // 2
        if get_gcd(mid, i) % x == 0:
            left = mid
            hi = mid - 1
        else:
            lo = mid + 1

    lo, hi = i, n - 1
    right = i
    while lo <= hi:
        mid = (lo + hi) // 2
        if get_gcd(i, mid) % x == 0:
            right = mid
            lo = mid + 1
        else:
            hi = mid - 1

    length = right - left
    if length > best:
        best = length
        starts = [left + 1]
    elif length == best:
        starts.append(left + 1)

starts = sorted(set(starts))
print(len(starts), best)
print(*starts)
