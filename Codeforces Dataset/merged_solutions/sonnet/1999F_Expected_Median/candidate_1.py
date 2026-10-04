# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

MOD = 10 ** 9 + 7

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    tests = []
    max_n = 0
    
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        ones = 0
        for _ in range(n):
            ones += data[idx]
            idx += 1
        
        tests.append((n, k, ones))
        max_n = max(max_n, n)
    
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    
    def comb(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
    
    answers = []
    for n, k, ones in tests:
        zeros = n - ones
        need = k // 2 + 1
        
        result = 0
        for take_ones in range(need, k + 1):
            result += comb(ones, take_ones) * comb(zeros, k - take_ones)
            result %= MOD
        
        answers.append(str(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
