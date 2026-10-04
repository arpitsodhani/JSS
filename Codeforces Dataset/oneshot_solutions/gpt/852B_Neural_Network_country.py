import sys

MOD = 10 ** 9 + 7

def conv(a, b, m):
    res = [0] * m
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    res[(i + j) % m] = (res[(i + j) % m] + ai * bj) % MOD
    return res

def power(base, exp, m):
    res = [0] * m
    res[0] = 1
    while exp:
        if exp & 1:
            res = conv(res, base, m)
        base = conv(base, base, m)
        exp >>= 1
    return res

data = list(map(int, sys.stdin.buffer.read().split()))
n, l, m = data[0], data[1], data[2]
a = data[3:3 + n]
b = data[3 + n:3 + 2 * n]
c = data[3 + 2 * n:3 + 3 * n]

first = [0] * m
middle = [0] * m
last = [0] * m

for x in a:
    first[x % m] += 1

for x in b:
    middle[x % m] += 1

for x, y in zip(b, c):
    last[(x + y) % m] += 1

for arr in (first, middle, last):
    for i in range(m):
        arr[i] %= MOD

ways = conv(first, power(middle, l - 2, m), m)
ways = conv(ways, last, m)
print(ways[0] % MOD)
