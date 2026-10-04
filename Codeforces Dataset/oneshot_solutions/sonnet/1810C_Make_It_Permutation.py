import sys
from collections import Counter

def solve():
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Count occurrences
    count = Counter(a)
    unique_vals = sorted(count.keys())
    
    # Cost to remove duplicates (keep only one of each value)
    dup_cost = sum((cnt - 1) * c for cnt in count.values())
    
    # Candidates for target permutation length k
    candidates = [1] + unique_vals
    
    # Try different permutation lengths
    min_cost = float('inf')
    
    for k in candidates:
        # Count how many unique values are in [1, k]
        keep = sum(1 for v in unique_vals if 1 <= v <= k)
        
        # Elements to remove: unique values not in [1, k]
        remove = len(unique_vals) - keep
        
        # Elements to insert: missing values from [1, k]
        insert = k - keep
        
        # Total cost
        cost = dup_cost + remove * c + insert * d
        min_cost = min(min_cost, cost)
    
    return min_cost

# Main
t = int(input())
for _ in range(t):
    print(solve())
