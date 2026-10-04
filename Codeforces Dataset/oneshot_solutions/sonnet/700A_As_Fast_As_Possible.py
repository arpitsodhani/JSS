import sys
import math

def main():
    n, l, v1, v2, k = map(int, sys.stdin.read().split())
    
    groups = (n + k - 1) // k
    
    if groups == 1:
        print("{:.10f}".format(l / v2))
        return
    
    low = 0.0
    high = l / v1
    
    for _ in range(100):
        mid = (low + high) / 2
        
        ride_time = (l - v1 * mid) / (v2 - v1)
        if ride_time <= 0:
            high = mid
            continue
        
        return_time = ride_time * (v2 - v1) / (v2 + v1)
        needed = groups * ride_time + (groups - 1) * return_time
        
        if needed <= mid:
            high = mid
        else:
            low = mid
    
    print("{:.10f}".format(high))

if __name__ == "__main__":
    main()
