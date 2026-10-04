import sys

MOD = 1000000009

def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n, w, b = map(int, data[:3])
    
    max_value = max(w, b, w + b)
    fact = [1] * (max_value + 1)
    for i in range(1, max_value + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact = [1] * (max_value + 1)
    inv_fact[max_value] = pow(fact[max_value], MOD - 2, MOD)
    for i in range(max_value, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    
    result = fact[w] * fact[b] % MOD
    result = result * (w - 1) % MOD
    result = result * comb(w + b - 3, n - 3, fact, inv_fact) % MOD
    
    print(result)

if __name__ == "__main__":
    main()
