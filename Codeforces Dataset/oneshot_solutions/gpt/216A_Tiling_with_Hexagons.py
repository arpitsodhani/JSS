import sys

a, b, c = map(int, sys.stdin.read().split())
print(a * b + b * c + c * a - a - b - c + 1)
