import sys
from collections import defaultdict

MOD = 998244353

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    weighted = defaultdict(int)
    count = defaultdict(int)
    
    inv_n = pow(n, MOD - 2, MOD)
    
    for _ in range(n):
        k = data[idx]
        idx += 1
        
        inv_k = pow(k, MOD - 2, MOD)
        add = inv_n * inv_k % MOD
        
        for _ in range(k):
            item = data[idx]
            idx += 1
            weighted[item] = (weighted[item] + add) % MOD
            count[item] += 1
    
    answer = 0
    for item, value in weighted.items():
        answer = (answer + value * count[item]) % MOD
    
    answer = answer * inv_n % MOD
    print(answer)

if __name__ == "__main__":
    main()
