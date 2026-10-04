import sys
from math import gcd

def main():
    a, b, x, y = map(int, sys.stdin.read().split())
    
    g = gcd(x, y)
    x //= g
    y //= g
    
    k = min(a // x, b // y)
    print(x * k, y * k)

if __name__ == "__main__":
    main()
