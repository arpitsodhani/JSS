import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, k = data[0], data[1]
a = data[2:]

print(2, a[0], a[1])
