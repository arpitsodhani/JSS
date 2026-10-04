from math import gcd

def solve(n, m):
    MOD = 998244353
    
    def coprime_count(p, max_val):
        """Count integers in [1, max_val] coprime to p"""
        count = 0
        for x in range(1, max_val + 1):
            if gcd(x, p) == 1:
                count += 1
        return count
    
    # dp[k] = number of non-ambiguous sequences of length k
    dp = [0] * (n + 1)
    dp[1] = m
    
    for k in range(2, n + 1):
        # For each position p that is the ONLY removable position initially
        for p in range(1, k + 1):
            ways = 1
            # a_p must be coprime to p
            ways = coprime_count(p, m)
            # All other a_i must NOT be coprime to i
            for i in range(1, k + 1):
                if i != p:
                    ways *= (m - coprime_count(i, m))
            # Multiply by number of non-ambiguous arrays of length k-1
            if ways > 0:
                dp[k] = (dp[k] + ways * dp[k - 1]) % MOD
    
    total = pow(m, n, MOD)
    ambiguous = (total - dp[n] + MOD) % MOD
    
    return ambiguous

n, m = map(int, input().split())
print(solve(n, m))
