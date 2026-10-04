import sys
from math import gcd

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    numbers = data[1:1 + n]
    
    g = 0
    for x in numbers:
        g = gcd(g, x)
    
    print(g * n)

if __name__ == "__main__":
    main()
