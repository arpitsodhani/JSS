from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

all_vals = [a[i][j] for i in range(n) for j in range(m)]
L = reduce(lcm, all_vals)
S = sum(x**4 for x in all_vals)

for i in range(n):
    print(' '.join(str(L * S - a[i][j]**4) for j in range(m)))
