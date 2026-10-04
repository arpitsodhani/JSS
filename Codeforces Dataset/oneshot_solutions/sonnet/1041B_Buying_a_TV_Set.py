import sys
from math import gcd

def main():
    a, b, x, y = map(int, sys.stdin.read().split())
    
    g = gcd(x, y)
    x //= g
    y //= g
    
    print(min(a // x, b // y))

main()
