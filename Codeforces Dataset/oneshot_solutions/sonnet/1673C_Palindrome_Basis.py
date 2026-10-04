import sys

MOD = 10 ** 9 + 7
MAX_N = 40000

def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

def main():
    palindromes = []
    for x in range(1, MAX_N + 1):
        if is_palindrome(x):
            palindromes.append(x)
    
    dp = [0] * (MAX_N + 1)
    dp[0] = 1
    
    for p in palindromes:
        for total in range(p, MAX_N + 1):
            dp[total] = (dp[total] + dp[total - p]) % MOD
    
    data = sys.stdin.read().split()
    t = int(data[0])
    result = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        result.append(str(dp[n]))
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
