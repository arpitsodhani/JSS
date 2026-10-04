import sys
from math import gcd

def factor_distinct(n):
    primes = []
    x = n
    
    d = 2
    while d * d <= x:
        if x % d == 0:
            primes.append(d)
            while x % d == 0:
                x //= d
        d += 1 if d == 2 else 2
    
    if x > 1:
        primes.append(x)
    
    return primes

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    primes = factor_distinct(n)
    
    if len(primes) < 2:
        print("NO")
        return
    
    p, q = primes[0], primes[1]
    b1 = n // p
    b2 = n // q
    
    g = gcd(p, q)
    p0 = p // g
    q0 = q // g
    target = (n - 1) // g
    
    # Find nonnegative x, y with x*p + y*q = n - 1
    inv = pow(p0, -1, q0)
    x = (target * inv) % q0
    y = (n - 1 - x * p) // q
    
    while y < 0:
        x += q0
        y = (n - 1 - x * p) // q
    
    ans = []
    
    while x > 0:
        take = min(x, b1 - 1)
        ans.append((take, b1))
        x -= take
    
    while y > 0:
        take = min(y, b2 - 1)
        ans.append((take, b2))
        y -= take
    
    print("YES")
    print(len(ans))
    for a, b in ans:
        print(a, b)

if __name__ == "__main__":
    main()
