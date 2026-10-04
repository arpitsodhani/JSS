import sys

MOD = 10 ** 9 + 7

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    statements = data[1:]
    
    dp = [0] * (n + 2)
    dp[0] = 1
    
    for i in range(n - 1):
        new_dp = [0] * (n + 2)
        
        if statements[i] == 'f':
            for indent in range(n):
                new_dp[indent + 1] = dp[indent]
        else:
            running = 0
            for indent in range(n, -1, -1):
                running = (running + dp[indent]) % MOD
                new_dp[indent] = running
        
        dp = new_dp
    
    print(sum(dp) % MOD)

if __name__ == "__main__":
    main()
