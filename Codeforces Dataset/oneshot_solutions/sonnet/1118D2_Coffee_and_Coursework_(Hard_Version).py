import sys

def can_finish(a, m, days):
    """Check if we can finish m pages in 'days' days."""
    total = 0
    for i in range(len(a)):
        penalty = i // days
        total += max(0, a[i] - penalty)
    return total >= m

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    a = [int(data[i+2]) for i in range(n)]
    
    # Sort in descending order
    a.sort(reverse=True)
    
    # Check if it's possible at all
    total_sum = sum(a)
    if total_sum < m:
        print(-1)
        return
    
    # Binary search on the number of days
    left, right = 1, n
    result = n
    
    while left <= right:
        mid = (left + right) // 2
        if can_finish(a, m, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(result)

solve()
