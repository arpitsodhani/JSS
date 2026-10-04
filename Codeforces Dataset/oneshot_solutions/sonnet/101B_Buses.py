import sys

def main():
    MOD = 10**9 + 7
    
    # Read input
    data = sys.stdin.buffer.read().decode().strip().split()
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    buses = []
    for _ in range(m):
        s = int(data[idx])
        t = int(data[idx + 1])
        buses.append((s, t))
        idx += 2
    
    # DP
    dp = [0] * (n + 1)
    dp[0] = 1
    
    # Group buses by ending stop
    buses_by_end = [[] for _ in range(n + 1)]
    for s, t in buses:
        buses_by_end[t].append(s)
    
    # Prefix sum for efficient range queries
    prefix = [0] * (n + 2)
    prefix[1] = dp[0]
    
    for i in range(1, n + 1):
        for s in buses_by_end[i]:
            # Sum of dp[j] for j in [s, i-1]
            range_sum = (prefix[i] - prefix[s] + MOD) % MOD
            dp[i] = (dp[i] + range_sum) % MOD
        
        prefix[i + 1] = (prefix[i] + dp[i]) % MOD
    
    print(dp[n])

if __name__ == "__main__":
    main()
