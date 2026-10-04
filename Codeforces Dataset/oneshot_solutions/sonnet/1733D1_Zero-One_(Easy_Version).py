import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        x = int(input_data[idx + 1])
        y = int(input_data[idx + 2])
        idx += 3
        
        a = input_data[idx]
        b = input_data[idx + 1]
        idx += 2
        
        # Find differing positions
        diff = [i for i in range(n) if a[i] != b[i]]
        k = len(diff)
        
        if k % 2 == 1:
            results.append(-1)
            continue
        
        if k == 0:
            results.append(0)
            continue
        
        # Cost function for pairing positions diff[i] and diff[j]
        def cost(i, j):
            if diff[j] == diff[i] + 1:
                return min(x, 2 * y)
            else:
                return y
        
        # DP: dp[i][j] = min cost to fix diff[i..j]
        INF = float('inf')
        dp = [[INF] * k for _ in range(k)]
        
        # Base case: single pair
        for i in range(k - 1):
            dp[i][i + 1] = cost(i, i + 1)
        
        # Fill DP for larger ranges (length must be even)
        for length in range(4, k + 1, 2):
            for i in range(k - length + 1):
                j = i + length - 1
                # Pair diff[i] with diff[m] where i < m <= j
                for m in range(i + 1, j + 1, 2):
                    left_cost = 0 if m == i + 1 else dp[i + 1][m - 1]
                    right_cost = 0 if m == j else dp[m + 1][j]
                    dp[i][j] = min(dp[i][j], cost(i, m) + left_cost + right_cost)
        
        results.append(dp[0][k - 1])
    
    print('\n'.join(map(str, results)))

solve()
