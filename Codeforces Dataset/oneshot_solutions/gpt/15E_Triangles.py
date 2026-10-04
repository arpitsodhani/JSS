import sys

MOD = 1000000009

n = int(sys.stdin.readline())
a = 2
b = 2
c = 4

for _ in range(n // 2 - 1):
    a = (a * 2) % MOD
    c = c * (a - 3) % MOD
    b = (b + c) % MOD

print((2 * (b * b + 1)) % MOD)
