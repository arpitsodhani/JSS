import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    s = sorted(data[1:1 + n])

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            dp[l][r] = min(dp[l + 1][r], dp[l][r - 1]) + s[r] - s[l]

    print(dp[0][n - 1])

if __name__ == "__main__":
    main()
