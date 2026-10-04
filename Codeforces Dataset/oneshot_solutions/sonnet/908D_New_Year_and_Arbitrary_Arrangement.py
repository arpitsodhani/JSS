import sys
from functools import lru_cache

sys.setrecursionlimit(100000)

k, pa, pb = map(int, input().split())

MOD = 10**9 + 7

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

total_inv = modinv(pa + pb)
p = (pa * total_inv) % MOD
q = (pb * total_inv) % MOD

p_div_q = (p * modinv(q)) % MOD

@lru_cache(maxsize=None)
def E(i, j):
    if j >= k:
        return j % MOD
    if i == 0:
        return E(1, j)
    if i >= k - j:
        return (i + j + p_div_q) % MOD
    return (p * E(i+1, j) + q * E(i, j+i)) % MOD

print(E(0, 0))
