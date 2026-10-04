def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    MOD = 998244353
    
    # dp[swap] for current position
    # swap = 0 means no swap, swap = 1 means swap
    prev_dp = [1, 1]  # Base case for position 0
    
    for i in range(1, n):
        curr_dp = [0, 0]
        for prev_swap in range(2):
            for curr_swap in range(2):
                # Calculate a' and b' for position i-1
                prev_a = a[i-1] if prev_swap == 0 else b[i-1]
                prev_b = b[i-1] if prev_swap == 0 else a[i-1]
                
                # Calculate a' and b' for position i
                curr_a = a[i] if curr_swap == 0 else b[i]
                curr_b = b[i] if curr_swap == 0 else a[i]
                
                # Check if transition is valid
                if curr_a >= prev_a and curr_b >= prev_b:
                    curr_dp[curr_swap] = (curr_dp[curr_swap] + prev_dp[prev_swap]) % MOD
        
        prev_dp = curr_dp
    
    return (prev_dp[0] + prev_dp[1]) % MOD

t = int(input())
for _ in range(t):
    print(solve())
