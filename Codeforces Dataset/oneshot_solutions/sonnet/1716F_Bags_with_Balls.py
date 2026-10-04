import sys

MOD = 998244353

def stirling_row(k):
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for x in range(1, k + 1):
        for i in range(x, 0, -1):
            dp[i] = (dp[i - 1] + i * dp[i]) % MOD
        dp[0] = 0
    
    return dp

def solve_case(n, m, k):
    if k == 0:
        return pow(m % MOD, n, MOD)
    
    odd = (m + 1) // 2
    odd %= MOD
    m_mod = m % MOD
    
    st = stirling_row(k)
    limit = min(k, n)
    
    if m_mod == 0:
        if n > k:
            return 0
        
        fact = 1
        odd_power = 1
        for i in range(1, n + 1):
            fact = fact * i % MOD
            odd_power = odd_power * odd % MOD
        
        return st[n] * fact % MOD * odd_power % MOD
    
    inv_m = pow(m_mod, MOD - 2, MOD)
    m_power = pow(m_mod, n, MOD)
    
    answer = 0
    falling = 1
    odd_power = 1
    
    for i in range(limit + 1):
        answer = (answer + st[i] * falling % MOD * odd_power % MOD * m_power) % MOD
        
        if i < limit:
            falling = falling * ((n - i) % MOD) % MOD
            odd_power = odd_power * odd % MOD
            m_power = m_power * inv_m % MOD
    
    return answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    
    results = []
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        k = data[idx + 2]
        idx += 3
        
        results.append(str(solve_case(n, m, k)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
