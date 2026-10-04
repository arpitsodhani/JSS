import sys

data = list(map(float, sys.stdin.read().split()))
l, p, q = data
print(l * p / (p + q))
