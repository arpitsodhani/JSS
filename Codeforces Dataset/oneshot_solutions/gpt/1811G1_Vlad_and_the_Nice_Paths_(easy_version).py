import sys
from math import comb

MOD = 10**9 + 7

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
ptr = 1
ans = []

for _ in range(t):
    n = data[ptr]
    k = data[ptr + 1]
    ptr += 2
    a = data[ptr:ptr + n]
    ptr += n

    dp = [0] * (n + 1)
    ways = [0] * (n + 1)
    ways[0] = 1

    pos = {}
    for i in range(1, n + 1):
        x = a[i - 1]
        pos.setdefault(x, []).append(i)

        dp[i] = dp[i - 1]
        ways[i] = ways[i - 1]

        occ = pos[x]
        if len(occ) >= k:
            l = occ[-k]
            cand = dp[l - 1] + 1
            add = ways[l - 1]
            if cand > dp[i]:
                dp[i] = cand
                ways[i] = add
            elif cand == dp[i]:
                ways[i] = (ways[i] + add) % MOD

    ans.append(str(ways[n] % MOD))

print("\n".join(ans))
