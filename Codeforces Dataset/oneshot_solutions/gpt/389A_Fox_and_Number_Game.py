import sys
import math

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:1 + n]

g = 0
for x in a:
    g = math.gcd(g, x)

print(g * n)
