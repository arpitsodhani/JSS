import sys
from math import gcd

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    result = []
    for i in range(1, t + 1):
        k = int(data[i])
        g = gcd(k, 100)
        result.append(str(100 // g))
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
