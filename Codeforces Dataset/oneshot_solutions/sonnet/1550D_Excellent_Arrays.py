import sys

MOD = 10**9 + 7

def prepare_combinations(max_n):
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    
    return fact, inv_fact

def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    tests = []
    idx = 1
    max_n = 0
    
    for _ in range(t):
        n = data[idx]
        l = data[idx + 1]
        r = data[idx + 2]
        idx += 3
        tests.append((n, l, r))
        max_n = max(max_n, n)
    
    fact, inv_fact = prepare_combinations(max_n)
    answers = []
    
    for n, l, r in tests:
        left_extra = 1 - l
        right_extra = r - n
        
        low = n // 2
        high = n - low
        common = min(left_extra, right_extra)
        
        balanced = comb(n, low, fact, inv_fact)
        if low != high:
            balanced = balanced * 2 % MOD
        
        result = common % MOD * balanced % MOD
        
        for x in range(common + 1, common + high + 1):
            forced_plus = max(0, x - left_extra)
            forced_minus = max(0, x - right_extra)
            free = n - forced_plus - forced_minus
            
            if free < 0:
                continue
            
            result = (result + comb(free, low - forced_plus, fact, inv_fact)) % MOD
            if low != high:
                result = (result + comb(free, high - forced_plus, fact, inv_fact)) % MOD
        
        answers.append(str(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
