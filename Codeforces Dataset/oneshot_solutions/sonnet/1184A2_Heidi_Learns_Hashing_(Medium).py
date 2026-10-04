import sys
from math import gcd

def solve():
    n = int(sys.stdin.readline())
    y = sys.stdin.readline().strip()
    
    count = 0
    for k in range(n):
        d = gcd(k, n)
        valid = True
        for s in range(d):
            xor_sum = 0
            pos = s
            for _ in range(n // d):
                xor_sum ^= int(y[pos])
                pos = (pos - k) % n
            if xor_sum != 0:
                valid = False
                break
        if valid:
            count += 1
    
    print(count)

solve()
