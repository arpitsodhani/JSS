def solve(n, d, a):
    a.sort()
    
    def can_achieve(target_mu):
        for remove_idx in range(n):
            remaining = [a[i] for i in range(n) if i != remove_idx]
            
            if not remaining:
                return d >= target_mu + 1
            
            # Before first exam
            if target_mu + 1 <= remaining[0] - target_mu - 1:
                return True
            
            # Between exams
            for i in range(len(remaining) - 1):
                if remaining[i] + target_mu + 1 <= remaining[i+1] - target_mu - 1:
                    return True
            
            # After last exam
            if remaining[-1] + target_mu + 1 <= d:
                return True
        
        return False
    
    left, right = 0, d
    while left < right:
        mid = (left + right + 1) // 2
        if can_achieve(mid):
            left = mid
        else:
            right = mid - 1
    
    return left

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, d, a))
