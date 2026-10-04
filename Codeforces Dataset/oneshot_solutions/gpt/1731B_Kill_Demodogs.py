import sys

MOD = 10**9 + 7
INV6 = pow(6, MOD - 2, MOD)

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

t = data[0]
ans = []

for n in data[1:1 + t]:
    val = n % MOD
    res = val * ((n + 1) % MOD) % MOD
    res = res * ((4 * n - 1) % MOD) % MOD
    res = res * INV6 % MOD
    res = res * 2022 % MOD
    ans.append(str(res))

print("\n".join(ans))
