import sys

v = list(map(int, sys.stdin.read().split()))
p = v[:4]
a, b = v[4], v[5]

m = min(p)
r = min(b, m - 1)

print(max(0, r - a + 1))
