def solve(n):
    for R in range(1, 100000):
        R_squared = R * R
        
        term = (n - 2) * (n - 1) // 2
        a_max = (R_squared - R - term) // n
        a_min = max(1, -(-max(0, R_squared - n * R + term) // n))
        
        if a_min > a_max:
            continue
        
        for a in range(a_min, a_max + 1):
            target_sum = R_squared - a - (a + R)
            remaining_count = n - 2
            
            if remaining_count == 0:
                if target_sum == 0:
                    return [a, a + R]
                else:
                    continue
            
            min_sum = sum(range(a + 1, a + 1 + remaining_count))
            max_sum = sum(range(a + R - remaining_count, a + R))
            
            if target_sum < min_sum or target_sum > max_sum:
                continue
            
            values = list(range(a + 1, a + 1 + remaining_count))
            current_sum = sum(values)
            diff = target_sum - current_sum
            
            for i in range(remaining_count - 1, -1, -1):
                max_increase = (a + R - 1) - values[i]
                if i < remaining_count - 1:
                    max_increase = min(max_increase, values[i + 1] - values[i] - 1)
                
                increase = min(diff, max_increase)
                values[i] += increase
                diff -= increase
                
                if diff == 0:
                    break
            
            if diff == 0:
                return [a] + values + [a + R]
    
    return None

import sys
input = sys.stdin.read
data = input().split()
idx = 0
t = int(data[idx])
idx += 1
for _ in range(t):
    n = int(data[idx])
    idx += 1
    result = solve(n)
    print(' '.join(map(str, result)))
