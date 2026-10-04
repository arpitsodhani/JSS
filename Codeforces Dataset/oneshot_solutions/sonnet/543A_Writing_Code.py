n, m, b, mod = map(int, input().split())
a = list(map(int, input().split()))

# dp[j][k] = number of ways to write j lines with k bugs
dp = [[0] * (b + 1) for _ in range(m + 1)]
dp[0][0] = 1

for i in range(n):
    bugs_per_line = a[i]
    for j in range(1, m + 1):
        for k in range(bugs_per_line, b + 1):
            dp[j][k] = (dp[j][k] + dp[j - 1][k - bugs_per_line]) % mod

ans = sum(dp[m][k] for k in range(b + 1)) % mod
print(ans)
