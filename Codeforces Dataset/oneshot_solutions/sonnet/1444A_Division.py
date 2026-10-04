import sys
import math
import random
from collections import Counter

def is_prime(n):
    if n < 2:
        return False
    
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n % p == 0:
            return n == p
    
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        
        ok = False
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                ok = True
                break
        
        if not ok:
            return False
    
    return True

def pollard(n):
    if n % 2 == 0:
        return 2
    
    while True:
        c = random.randrange(1, n - 1)
        x = random.randrange(0, n - 1)
        y = x
        d = 1
        
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
        
        if d != n:
            return d

def factor(n, result):
    if n == 1:
        return
    
    if is_prime(n):
        result.append(n)
        return
    
    d = pollard(n)
    factor(d, result)
    factor(n // d, result)

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    
    answers = []
    for _ in range(t):
        p = int(data[idx])
        q = int(data[idx + 1])
        idx += 2
        
        if p % q != 0:
            answers.append(str(p))
            continue
        
        factors = []
        factor(q, factors)
        
        best = 1
        for prime in set(factors):
            cur = p
            while cur % q == 0:
                cur //= prime
            best = max(best, cur)
        
        answers.append(str(best))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
