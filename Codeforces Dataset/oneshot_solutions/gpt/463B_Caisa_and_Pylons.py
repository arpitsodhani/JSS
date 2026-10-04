import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
h = data[1:1 + n]
print(max(h))
