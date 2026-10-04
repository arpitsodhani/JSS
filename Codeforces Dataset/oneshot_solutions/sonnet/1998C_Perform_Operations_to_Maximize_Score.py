import sys
from bisect import bisect_left

def median_after_deleting(rank, sorted_values, m):
    if rank <= m - 1:
        return sorted_values[m]
    return sorted_values[m - 1]

def solve_case(n, k, a, b):
    m = n // 2
    need = n - m
    
    order = sorted(range(n), key=lambda i: a[i])
    sorted_values = [a[i] for i in order]
    rank = [0] * n
    for r, i in enumerate(order):
        rank[i] = r
    
    ans = 0
    
    for i in range(n):
        if b[i] == 1:
            med = median_after_deleting(rank[i], sorted_values, m)
            ans = max(ans, a[i] + k + med)
    
    best_zero = -1
    for i in range(n):
        if b[i] == 0 and (best_zero == -1 or a[i] > a[best_zero]):
            best_zero = i
    
    if best_zero != -1:
        one_values = sorted(a[i] for i in range(n) if b[i] == 1)
        prefix = [0]
        for x in one_values:
            prefix.append(prefix[-1] + x)
        
        removed = a[best_zero]
        
        def can_make(x):
            total_ge = n - bisect_left(sorted_values, x)
            if removed >= x:
                total_ge -= 1
            
            add = need - total_ge
            if add <= 0:
                return True
            
            pos = bisect_left(one_values, x)
            if pos < add:
                return False
            
            have_sum = prefix[pos] - prefix[pos - add]
            return add * x - have_sum <= k
        
        low = 0
        high = max(a) + k + 1
        while low + 1 < high:
            mid = (low + high) // 2
            if can_make(mid):
                low = mid
            else:
                high = mid
        
        ans = max(ans, removed + low)
    
    return ans

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        
        b = data[idx:idx + n]
        idx += n
        
        out.append(str(solve_case(n, k, a, b)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
