import sys

def solve(n, s, a):
    MOD = 10**9 + 7
    
    # Precompute min_allowed[i][j] = min(a[ord(s[k]) - ord('a')] for k in [i,j])
    min_allowed = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        min_allowed[i][i] = a[ord(s[i]) - ord('a')]
        for j in range(i + 1, n):
            min_allowed[i][j] = min(min_allowed[i][j-1], a[ord(s[j]) - ord('a')])
    
    # DP arrays
    min_dp = [float('inf')] * (n + 1)
    max_dp = [-1] * (n + 1)
    ways_to_min = [0] * (n + 1)
    
    min_dp[0] = 0
    max_dp[0] = 0
    ways_to_min[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            # Check if s[j:i] is valid
            length = i - j
            if min_allowed[j][i-1] >= length:
                # Update min_dp and ways_to_min
                if min_dp[j] + 1 < min_dp[i]:
                    min_dp[i] = min_dp[j] + 1
                    ways_to_min[i] = ways_to_min[j]
                elif min_dp[j] + 1 == min_dp[i]:
                    ways_to_min[i] = (ways_to_min[i] + ways_to_min[j]) % MOD
                
                # Update max_dp
                max_dp[i] = max(max_dp[i], max_dp[j] + 1)
    
    return max_dp[n], min_dp[n], ways_to_min[n]

# Read input
input_data = sys.stdin.read().split()
idx = 0
n = int(input_data[idx])
idx += 1
s = input_data[idx]
idx += 1
a = [int(input_data[idx + i]) for i in range(26)]

max_parts, min_parts, ways = solve(n, s, a)
print(max_parts)
print(min_parts)
print(ways)
