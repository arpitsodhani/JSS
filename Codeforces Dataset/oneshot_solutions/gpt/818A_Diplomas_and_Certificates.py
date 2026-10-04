import sys

n, k = map(int, sys.stdin.read().split())

d = (n // 2) // (k + 1)
c = d * k
r = n - d - c

print(d, c, r)
