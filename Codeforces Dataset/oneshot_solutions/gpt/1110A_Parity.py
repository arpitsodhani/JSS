import sys

data = list(map(int, sys.stdin.read().split()))
b, k = data[0], data[1]
a = data[2:2 + k]

if b % 2 == 0:
    parity = a[-1] % 2
else:
    parity = sum(a) % 2

print("odd" if parity else "even")
