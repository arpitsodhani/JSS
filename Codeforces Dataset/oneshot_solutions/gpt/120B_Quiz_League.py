import sys

data = list(map(int, sys.stdin.read().split()))
n, k = data[0], data[1]
a = data[2:]

pos = (k - 1) % n
while a[pos]:
    pos = (pos + 1) % n

print(pos + 1)
