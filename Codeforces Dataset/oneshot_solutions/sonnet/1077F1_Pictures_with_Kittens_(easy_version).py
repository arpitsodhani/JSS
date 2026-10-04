import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n, k, x = data[0], data[1], data[2]
    a = [0] + data[3:3 + n]
    
    neg = -10 ** 30
    dp = [[neg] * (n + 1) for _ in range(x + 1)]
    
    for i in range(1, min(n, k) + 1):
        dp[1][i] = a[i]
    
    for taken in range(2, x + 1):
        for i in range(1, n + 1):
            best = neg
            left = max(1, i - k)
            for prev in range(left, i):
                if dp[taken - 1][prev] > best:
                    best = dp[taken - 1][prev]
            if best != neg:
                dp[taken][i] = best + a[i]
    
    answer = max(dp[x][max(1, n - k + 1):n + 1])
    print(answer if answer != neg else -1)

if __name__ == "__main__":
    main()
