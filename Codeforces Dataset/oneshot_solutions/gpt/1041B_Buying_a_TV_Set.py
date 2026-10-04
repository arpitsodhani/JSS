import sys
from math import gcd

a, b, x, y = map(int, sys.stdin.readline().split())
g = gcd(x, y)
x //= g
y //= g
print(min(a // x, b // y))
