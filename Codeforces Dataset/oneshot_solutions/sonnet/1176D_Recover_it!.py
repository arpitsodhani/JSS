import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    nums = data[1:]
    
    limit = max(nums)
    spf = list(range(limit + 1))
    primes = []
    prime_index = [0] * (limit + 1)
    
    for i in range(2, limit + 1):
        if spf[i] == i:
            prime_index[i] = len(primes) + 1
            primes.append(i)
        for p in primes:
            v = i * p
            if v > limit or p > spf[i]:
                break
            spf[v] = p
    
    count = Counter(nums)
    result = []
    
    for x in sorted(nums, reverse=True):
        if count[x] == 0:
            continue
        
        count[x] -= 1
        
        if spf[x] == x:
            idx = prime_index[x]
            result.append(idx)
            count[idx] -= 1
        else:
            result.append(x)
            divisor = x // spf[x]
            count[divisor] -= 1
        
        if len(result) == n:
            break
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
