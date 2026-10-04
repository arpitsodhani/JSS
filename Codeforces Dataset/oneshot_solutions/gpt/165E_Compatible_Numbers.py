import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
a = data[1:1 + n]

B = 22
M = 1 << B
full = M - 1

dp = [-1] * M
for x in a:
    dp[x] = x

for b in range(B):
    step = 1 << b
    for mask in range(M):
        if mask & step and dp[mask] == -1:
            dp[mask] = dp[mask ^ step]

print(*[dp[full ^ x] for x in a])
