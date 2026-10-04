import sys
from math import isqrt

def smallest_divisor(n):
    if n % 2 == 0:
        return 2
    
    d = 3
    limit = isqrt(n)
    while d <= limit:
        if n % d == 0:
            return d
        d += 2
    
    return n

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        if n % 2 == 0:
            results.append(str(n + 2 * k))
        else:
            n += smallest_divisor(n)
            results.append(str(n + 2 * (k - 1)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
