import sys

a, b, c, d, e, f = map(int, sys.stdin.read().split())

if b * d * f > a * c * e:
    print("Ron")
else:
    print("Hermione")
