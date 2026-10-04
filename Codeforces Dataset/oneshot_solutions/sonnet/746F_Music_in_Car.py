import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n, w, k = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3
    
    a = [int(data[idx + i]) for i in range(n)]
    idx += n
    t = [int(data[idx + i]) for i in range(n)]
    
    max_pleasure = 0
    
    # Try each starting position
    for start in range(n):
        m = n - start  # number of songs available
        
        INF = float('inf')
        # dp[i][j] = minimum time for first i songs using exactly j partials
        dp = [[INF] * (min(w, m) + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        
        # Precompute prefix sums for pleasure
        pleasure_sum = [0]
        for i in range(m):
            pleasure_sum.append(pleasure_sum[-1] + a[start + i])
        
        for i in range(m):
            song_idx = start + i
            for j in range(min(w, i) + 1):
                if dp[i][j] == INF:
                    continue
                
                # Option 1: listen fully
                full_time = dp[i][j] + t[song_idx]
                if full_time <= k:
                    dp[i+1][j] = min(dp[i+1][j], full_time)
                
                # Option 2: listen partially (if we have partials left)
                if j < w:
                    partial_time = dp[i][j] + (t[song_idx] + 1) // 2
                    if partial_time <= k:
                        dp[i+1][j+1] = min(dp[i+1][j+1], partial_time)
        
        # Find max pleasure for each valid state
        for i in range(1, m + 1):
            for j in range(min(w, i) + 1):
                if dp[i][j] <= k:
                    max_pleasure = max(max_pleasure, pleasure_sum[i])
    
    print(max_pleasure)

solve()
