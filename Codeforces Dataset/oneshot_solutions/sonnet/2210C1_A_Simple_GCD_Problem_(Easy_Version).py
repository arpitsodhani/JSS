import sys
from math import gcd

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = list(map(int, input_data[idx:idx+n]))
        idx += n
        b = list(map(int, input_data[idx:idx+n]))
        idx += n
        
        count = 0
        for i in range(n):
            if n == 1:
                if b[i] > 1:
                    count += 1
                continue
            
            has_adjacent_equal = False
            if i > 0 and a[i] == a[i-1]:
                has_adjacent_equal = True
            if i < n-1 and a[i] == a[i+1]:
                has_adjacent_equal = True
            
            if has_adjacent_equal:
                continue
            
            if i == 0:
                g = gcd(a[0], a[1])
            elif i == n-1:
                g = gcd(a[n-2], a[n-1])
            else:
                g = gcd(gcd(a[i-1], a[i]), a[i+1])
            
            if g < a[i] and g <= b[i]:
                count += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

solve()
