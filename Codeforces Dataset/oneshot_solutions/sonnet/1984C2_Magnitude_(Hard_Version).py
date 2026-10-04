import sys
from collections import defaultdict

MOD = 998244353

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        # dp[value] = count of procedures leading to this value
        dp = defaultdict(int)
        dp[0] = 1
        
        for ai in a:
            new_dp = defaultdict(int)
            for c, cnt in dp.items():
                # Option 1: c + ai
                v1 = c + ai
                new_dp[v1] = (new_dp[v1] + cnt) % MOD
                
                # Option 2: |c + ai|
                v2 = abs(c + ai)
                new_dp[v2] = (new_dp[v2] + cnt) % MOD
            
            dp = new_dp
        
        max_val = max(dp.keys())
        result = dp[max_val]
        results.append(str(result))
    
    print('\n'.join(results))

solve()
