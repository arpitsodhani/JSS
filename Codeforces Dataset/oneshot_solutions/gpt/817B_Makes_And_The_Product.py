import sys
from collections import Counter
from math import comb

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:]

a.sort()
x, y, z = a[0], a[1], a[2]
cnt = Counter(a)

if x == y == z:
    print(comb(cnt[x], 3))
elif x == y:
    print(comb(cnt[x], 2) * cnt[z])
elif y == z:
    print(cnt[x] * comb(cnt[y], 2))
else:
    print(cnt[x] * cnt[y] * cnt[z])
