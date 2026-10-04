# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
MOD = 1000000007

def is_lucky(x):
    if x <= 0:
        return False
    while x:
        d = x % 10
        if d != 4 and d != 7:
            return False
        x //= 10
    return True
data = list(map(int, sys.stdin.buffer.read().split()))
n, k = (data[0], data[1])
a = data[2:2 + n]
cnt = Counter()
unlucky = 0
for x in a:
    if is_lucky(x):
        cnt[x] += 1
    else:
        unlucky += 1
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact = [1] * (n + 1)
invfact[n] = pow(fact[n], MOD - 2, MOD)
for i in range(n, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

def comb(nn, rr):
    if rr < 0 or rr > nn:
        return 0
    return fact[nn] * invfact[rr] % MOD * invfact[nn - rr] % MOD
limit = min(k, len(cnt))
dp = [0] * (limit + 1)
dp[0] = 1
for c in cnt.values():
    for j in range(limit, 0, -1):
        dp[j] = (dp[j] + dp[j - 1] * c) % MOD
ans = 0
for lucky_taken in range(limit + 1):
    ans = (ans + dp[lucky_taken] * comb(unlucky, k - lucky_taken)) % MOD
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
