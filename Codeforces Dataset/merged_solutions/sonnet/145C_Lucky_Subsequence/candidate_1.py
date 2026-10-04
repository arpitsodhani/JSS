# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

MOD = 1000000007

def is_lucky(x):
    if x <= 0:
        return False
    while x:
        d = x % 10
        if d != 4 and d != 7:
            return False
        x //= 10
    return True

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    a = data[2:]
    
    lucky_count = {}
    unlucky = 0
    
    for x in a:
        if is_lucky(x):
            lucky_count[x] = lucky_count.get(x, 0) + 1
        else:
            unlucky += 1
    
    max_n = n
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    
    def comb(nn, rr):
        if rr < 0 or rr > nn:
            return 0
        return fact[nn] * inv_fact[rr] % MOD * inv_fact[nn - rr] % MOD
    
    dp = [0] * (len(lucky_count) + 1)
    dp[0] = 1
    
    used = 0
    for cnt in lucky_count.values():
        for j in range(used, -1, -1):
            dp[j + 1] = (dp[j + 1] + dp[j] * cnt) % MOD
        used += 1
    
    ans = 0
    for lucky_taken in range(min(k, len(lucky_count)) + 1):
        ans = (ans + dp[lucky_taken] * comb(unlucky, k - lucky_taken)) % MOD
    
    print(ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
