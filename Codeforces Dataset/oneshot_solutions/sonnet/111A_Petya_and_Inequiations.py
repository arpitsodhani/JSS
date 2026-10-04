import sys
from math import isqrt

def main():
    data = list(map(int, sys.stdin.read().split()))
    n, x, y = data
    
    if y < n:
        print(-1)
        return
    
    big = y - n + 1
    if big * big + (n - 1) < x:
        print(-1)
        return
    
    result = [1] * n
    result[0] = big
    print(' '.join(map(str, result)))

main()
