import sys

def solve():
    n = int(sys.stdin.readline())
    speeds = list(map(int, sys.stdin.readline().split()))
    
    speeds.sort()
    
    if n == 1:
        print(0)
        return
    
    # dp[l][r] = minimum cost to arrange elements from l to r
    dp = [[0] * n for _ in range(n)]
    
    # Base case: single elements have cost 0
    for i in range(n):
        dp[i][i] = 0
    
    # Fill DP table by increasing length
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            # Option 1: pick l first, then arrange [l+1, r]
            cost1 = dp[l+1][r] + (r - l) * (speeds[l+1] - speeds[l])
            # Option 2: pick r first, then arrange [l, r-1]
            cost2 = dp[l][r-1] + (r - l) * (speeds[r] - speeds[r-1])
            dp[l][r] = min(cost1, cost2)
    
    print(dp[0][n-1])

solve()
