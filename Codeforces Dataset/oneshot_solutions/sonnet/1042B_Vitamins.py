def solve():
    n = int(input())
    juices = []
    
    for _ in range(n):
        line = input().split()
        cost = int(line[0])
        vitamins = line[1]
        
        mask = 0
        if 'A' in vitamins:
            mask |= 1
        if 'B' in vitamins:
            mask |= 2
        if 'C' in vitamins:
            mask |= 4
        
        juices.append((cost, mask))
    
    # dp[mask] = minimum cost to get vitamins represented by mask
    INF = float('inf')
    dp = [INF] * 8
    dp[0] = 0
    
    for cost, mask in juices:
        # Process this juice
        new_dp = dp[:]
        for state in range(8):
            if dp[state] < INF:
                new_state = state | mask
                new_dp[new_state] = min(new_dp[new_state], dp[state] + cost)
        dp = new_dp
    
    if dp[7] == INF:
        print(-1)
    else:
        print(dp[7])

solve()
