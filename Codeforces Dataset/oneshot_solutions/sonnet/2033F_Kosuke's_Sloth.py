import sys
from math import gcd

MOD = 10**9 + 7

def rank_zero(k):
    if k == 1:
        return 1
    
    a, b = 0, 1
    for i in range(1, 6 * k + 1):
        a, b = b, (a + b) % k
        if a == 0:
            return i

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    cache = {}
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        if k not in cache:
            cache[k] = rank_zero(k)
        
        out.append(str((n % MOD) * (cache[k] % MOD) % MOD))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
