import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    A = int(input_data[idx])
    idx += 1
    B = int(input_data[idx])
    idx += 1
    n = int(input_data[idx])
    idx += 1
    
    results = []
    
    for _ in range(n):
        l = int(input_data[idx])
        idx += 1
        t = int(input_data[idx])
        idx += 1
        m = int(input_data[idx])
        idx += 1
        
        # s_i = A + (i-1)*B
        s_l = A + (l - 1) * B
        
        # Check if s_l > t
        if s_l > t:
            results.append(-1)
            continue
        
        # Binary search for the largest r
        left, right = l, 2 * 10**9
        
        # Constraint: max(s_i for i in [l, r]) <= t
        if B > 0:
            # s_r = A + (r-1)*B <= t => r <= (t - A) / B + 1
            right = min(right, (t - A) // B + 1)
        
        ans = l
        
        while left <= right:
            mid = (left + right) // 2
            
            s_mid = A + (mid - 1) * B
            
            # Total sum <= t * m
            # Sum = (mid - l + 1) * (s_l + s_mid) / 2 <= t * m
            # Equivalent: (mid - l + 1) * (s_l + s_mid) <= 2 * t * m
            count = mid - l + 1
            if count * (s_l + s_mid) <= 2 * t * m:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        results.append(ans)
    
    for res in results:
        print(res)

solve()
