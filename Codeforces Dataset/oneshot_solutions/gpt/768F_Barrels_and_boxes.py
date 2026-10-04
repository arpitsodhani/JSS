import sys
from array import array

MOD = 1000000007

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

f, w, h = data[:3]

if w == 0:
    print(1)
    sys.exit()

if f == 0:
    print(1 if w > h else 0)
    sys.exit()

nmax = f + w - 2

fact = array('I', [1]) * (nmax + 1)
for i in range(1, nmax + 1):
    fact[i] = (fact[i - 1] * i) % MOD

invfact = array('I', [1]) * (nmax + 1)
invfact[nmax] = pow(fact[nmax], MOD - 2, MOD)
for i in range(nmax, 0, -1):
    invfact[i - 1] = (invfact[i] * i) % MOD

def c(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD

nf = f - 1
nw = w - 1
total_n = f + w - 2

den = (c(total_n, nf - 1) + 2 * c(total_n, nf) + c(total_n, nf + 1)) % MOD

limit = w // (h + 1) if h + 1 > 0 else w
num = 0

for b in range(1, limit + 1):
    wine = c(w - b * h - 1, b - 1)
    food = (c(f - 1, b - 2) + 2 * c(f - 1, b - 1) + c(f - 1, b)) % MOD
    num = (num + wine * food) % MOD

print(num * pow(den, MOD - 2, MOD) % MOD)
