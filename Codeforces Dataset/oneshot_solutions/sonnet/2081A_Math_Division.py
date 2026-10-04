import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

MOD = 10**9 + 7
inv2 = pow(2, MOD - 2, MOD)

@lru_cache(maxsize=None)
def expected_ops(x):
    if x == 1:
        return 0
    if x % 2 == 0:
        return (1 + expected_ops(x // 2)) % MOD
    else:
        e1 = expected_ops(x // 2)
        e2 = expected_ops((x + 1) // 2)
        return (1 + (e1 + e2) * inv2) % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    binary = input().strip()
    x = int(binary, 2)
    print(expected_ops(x))
