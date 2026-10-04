import sys

b, k = map(int, sys.stdin.readline().split())
digits = list(map(int, sys.stdin.readline().split()))

if b % 2 == 0:
    parity = digits[-1] % 2
else:
    parity = sum(digits) % 2

print("even" if parity == 0 else "odd")
