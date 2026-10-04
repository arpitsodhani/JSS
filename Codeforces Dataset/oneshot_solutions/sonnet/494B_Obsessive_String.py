import sys

MOD = 10 ** 9 + 7

def build_occurrences(s, t):
    n = len(s)
    m = len(t)
    
    pi = [0] * m
    for i in range(1, m):
        j = pi[i - 1]
        while j > 0 and t[i] != t[j]:
            j = pi[j - 1]
        if t[i] == t[j]:
            j += 1
        pi[i] = j
    
    latest_start = [0] * (n + 1)
    j = 0
    last = 0
    
    for i in range(n):
        while j > 0 and s[i] != t[j]:
            j = pi[j - 1]
        if s[i] == t[j]:
            j += 1
        
        if j == m:
            last = i - m + 2
            j = pi[j - 1]
        
        latest_start[i + 1] = last
    
    return latest_start

def main():
    data = sys.stdin.read().split()
    s = data[0]
    t = data[1]
    
    n = len(s)
    latest_start = build_occurrences(s, t)
    
    dp = [0] * (n + 1)
    prefix_dp = [0] * (n + 1)
    prefix_add = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_add[i] = (prefix_add[i - 1] + prefix_dp[i - 1] + 1) % MOD
        
        start = latest_start[i]
        dp[i] = dp[i - 1]
        if start > 0:
            dp[i] = (dp[i] + prefix_add[start]) % MOD
        
        prefix_dp[i] = dp[i]
    
    print(dp[n] % MOD)

if __name__ == "__main__":
    main()
