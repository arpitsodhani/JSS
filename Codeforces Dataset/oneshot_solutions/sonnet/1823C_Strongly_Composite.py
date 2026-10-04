import sys
from collections import defaultdict
from math import isqrt

def build_primes(limit):
    is_prime = [True] * (limit + 1)
    primes = []
    
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            step = i
            start = i * i
            if start <= limit:
                is_prime[start:limit + 1:step] = [False] * (((limit - start) // step) + 1)
    
    return primes

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    t = data[0]
    idx = 1
    
    values = []
    scan = idx
    for _ in range(t):
        n = data[scan]
        scan += 1
        values.extend(data[scan:scan + n])
        scan += n
    
    primes = build_primes(isqrt(max(values)) + 1 if values else 2)
    
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        count = defaultdict(int)
        for _ in range(n):
            x = data[idx]
            idx += 1
            
            for p in primes:
                if p * p > x:
                    break
                while x % p == 0:
                    count[p] += 1
                    x //= p
            
            if x > 1:
                count[x] += 1
        
        pairs = 0
        leftovers = 0
        for c in count.values():
            pairs += c // 2
            leftovers += c % 2
        
        out.append(str(pairs + leftovers // 3))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
