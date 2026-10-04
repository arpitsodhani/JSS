import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    
    # Build prefix sum array
    prefix = [0]
    for x in a:
        prefix.append(prefix[-1] + x)
    
    max_sum = 0
    
    # Try all possible distributions of operations
    for x in range(k + 1):
        left_remove = 2 * x  # Elements removed from left (smallest)
        right_remove = k - x  # Elements removed from right (largest)
        
        # Check if valid
        if left_remove + right_remove > n:
            continue
        
        # Calculate sum of removed elements
        sum_removed = prefix[left_remove] + (prefix[n] - prefix[n - right_remove])
        remaining_sum = prefix[n] - sum_removed
        max_sum = max(max_sum, remaining_sum)
    
    return max_sum

t = int(input())
for _ in range(t):
    print(solve())
