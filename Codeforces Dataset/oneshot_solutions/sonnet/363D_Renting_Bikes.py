import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    n = data[idx]; idx += 1
    m = data[idx]; idx += 1
    a = data[idx]; idx += 1
    b = data[idx:idx+n]; idx += n
    p = data[idx:idx+m]; idx += m
    
    def can_afford(k):
        if k == 0:
            return True
        # Select top k boys by personal money
        boys = sorted(b, reverse=True)[:k]
        # Select k cheapest bikes
        bikes = sorted(p)[:k]
        
        # Sort both ascending for optimal matching
        boys_sorted = sorted(boys)
        bikes_sorted = sorted(bikes)
        
        # Minimum shared budget needed
        min_shared = sum(max(0, bikes_sorted[i] - boys_sorted[i]) for i in range(k))
        
        return min_shared <= a
    
    # Binary search on number of boys
    left, right = 0, min(n, m)
    max_k = 0
    while left <= right:
        mid = (left + right) // 2
        if can_afford(mid):
            max_k = mid
            left = mid + 1
        else:
            right = mid - 1
    
    if max_k == 0:
        print(0, 0)
    else:
        boys = sorted(b, reverse=True)[:max_k]
        bikes = sorted(p)[:max_k]
        total_cost = sum(bikes)
        min_personal = max(0, total_cost - a)
        print(max_k, min_personal)

solve()
