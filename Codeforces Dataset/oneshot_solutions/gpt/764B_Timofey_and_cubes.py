import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
a = data[1:]

l, r = 0, n - 1
while l < r:
    a[l], a[r] = a[r], a[l]
    l += 2
    r -= 2

print(*a)
