import sys
from math import isqrt

def find_pair(x):
    d = 1
    while d * d <= x:
        if x % d == 0:
            a = d
            b = x // d
            
            if (a + b) % 2 == 0:
                n = (a + b) // 2
                k = (b - a) // 2
                
                if k >= 1:
                    left = n // (k + 1) + 1
                    right = n // k
                    
                    if left <= right:
                        return n, left
        d += 1
    
    return None

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    x = int(data[0])
    result = find_pair(x)
    
    if result is None:
        print(-1)
    else:
        print(result[0], result[1])

if __name__ == "__main__":
    main()
