def solve():
    n = int(input())
    s = input().strip()
    costs = list(map(int, input().split()))
    
    target = "hard"
    INF = float('inf')
    
    # dp[j] = min cost to have matched j characters of "hard" so far
    dp = [0, INF, INF, INF]
    
    for i in range(n):
        new_dp = [INF, INF, INF, INF]
        
        for j in range(4):
            if dp[j] == INF:
                continue
            
            # Option 1: Remove character i
            new_dp[j] = min(new_dp[j], dp[j] + costs[i])
            
            # Option 2: Keep character i
            if s[i] == target[j]:
                # This character matches the next character in "hard"
                if j + 1 < 4:
                    new_dp[j+1] = min(new_dp[j+1], dp[j])
            else:
                # This character doesn't match, stay at same state
                new_dp[j] = min(new_dp[j], dp[j])
        
        dp = new_dp
    
    print(min(dp))

solve()
