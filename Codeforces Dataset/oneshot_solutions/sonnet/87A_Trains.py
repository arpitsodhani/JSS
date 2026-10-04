import sys
from math import gcd

def attraction(period, other):
    if other <= 1:
        return 0
    
    last = other - 1
    if last <= period:
        return last * (last + 1) // 2
    
    return period * (period + 1) // 2 + period * (last - period)

def main():
    data = sys.stdin.read().split()
    a = int(data[0])
    b = int(data[1])
    
    if a == b:
        print("Equal")
        return
    
    g = gcd(a, b)
    a //= g
    b //= g
    
    dasha = attraction(a, b)
    masha = attraction(b, a)
    
    last_gap = min(a, b)
    if a > b:
        dasha += last_gap
    else:
        masha += last_gap
    
    if dasha > masha:
        print("Dasha")
    elif masha > dasha:
        print("Masha")
    else:
        print("Equal")

if __name__ == "__main__":
    main()
