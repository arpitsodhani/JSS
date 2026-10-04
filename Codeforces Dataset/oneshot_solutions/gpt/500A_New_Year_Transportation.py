import sys

data = list(map(int, sys.stdin.read().split()))
n, t = data[0], data[1]
a = data[2:]

pos = 1
while pos < t:
    pos += a[pos - 1]

print("YES" if pos == t else "NO")
