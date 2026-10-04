MOD = 10**9 + 7

def count_mod(l, r, k):
    # Count numbers in [l, r] with remainder k mod 3
    first = l + (k - l % 3 + 3) % 3
    if first > r:
        return 0
    return (r - first) // 3 + 1

n, l, r = map(int, input().split())

c0 = count_mod(l, r, 0)
c1 = count_mod(l, r, 1)
c2 = count_mod(l, r, 2)

dp = [0] * 3
dp[0] = 1

for i in range(n):
    new_dp = [0] * 3
    for j in range(3):
        new_dp[j] = (c0 * dp[j] + c1 * dp[(j-1+3)%3] + c2 * dp[(j-2+3)%3]) % MOD
    dp = new_dp

print(dp[0])
