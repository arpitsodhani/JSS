import sys
from functools import lru_cache

MOD = 998244353

def calc(n, k):
    if n <= 0:
        return 0
    
    digits = list(map(int, str(n)))
    length = len(digits)
    pow10 = [1] * (length + 1)
    for i in range(1, length + 1):
        pow10[i] = pow10[i - 1] * 10 % MOD
    
    @lru_cache(None)
    def dp(pos, mask, started, tight):
        if pos == length:
            return (1, 0)
        
        limit = digits[pos] if tight else 9
        rem = length - pos - 1
        
        total_count = 0
        total_sum = 0
        
        for d in range(limit + 1):
            ntight = tight and d == limit
            
            if not started and d == 0:
                count, value_sum = dp(pos + 1, mask, False, ntight)
                total_count = (total_count + count) % MOD
                total_sum = (total_sum + value_sum) % MOD
            else:
                new_mask = mask | (1 << d)
                if new_mask.bit_count() > k:
                    continue
                
                count, value_sum = dp(pos + 1, new_mask, True, ntight)
                add = (d * pow10[rem] * count + value_sum) % MOD
                total_count = (total_count + count) % MOD
                total_sum = (total_sum + add) % MOD
        
        return (total_count, total_sum)
    
    return dp(0, 0, False, True)[1]

def main():
    l, r, k = map(int, sys.stdin.read().split())
    print((calc(r, k) - calc(l - 1, k)) % MOD)

if __name__ == "__main__":
    main()
