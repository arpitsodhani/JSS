import sys

data = sys.stdin.read().split()
x, y = data[0], data[1]

if all(b <= a for a, b in zip(x, y)):
    print(y)
else:
    print(-1)
