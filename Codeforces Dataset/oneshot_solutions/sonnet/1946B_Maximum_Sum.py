def solve():
    MOD = 10**9 + 7
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Calculate original sum
    total_sum = sum(a)
    
    # Find maximum subarray sum using Kadane's algorithm
    max_ending_here = 0
    max_so_far = 0
    for x in a:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    
    # Total contribution: max_so_far * (2^k - 1)
    power_of_2 = pow(2, k, MOD)
    multiplier = (power_of_2 - 1 + MOD) % MOD
    contribution = (max_so_far % MOD * multiplier) % MOD
    result = (total_sum % MOD + contribution) % MOD
    
    return result

t = int(input())
for _ in range(t):
    print(solve())
