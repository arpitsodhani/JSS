import sys
from bisect import bisect_left, bisect_right

def solve():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n, l, r = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        a = [int(data[idx+i]) for i in range(n)]
        idx += n
        
        a.sort()
        count = 0
        
        for i in range(n):
            min_val = l - a[i]
            max_val = r - a[i]
            
            left = bisect_left(a, min_val, i+1, n)
            right = bisect_right(a, max_val, i+1, n) - 1
            
            if left <= right:
                count += right - left + 1
        
        print(count)

solve()
