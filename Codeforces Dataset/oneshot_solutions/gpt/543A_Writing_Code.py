import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n, m, b, mod = data[:4]
    a = data[4:4 + n]

    dp = [[0] * (b + 1) for _ in range(m + 1)]
    dp[0][0] = 1

    for bugs_per_line in a:
        for lines in range(1, m + 1):
            prev = dp[lines - 1]
            cur = dp[lines]
            for bugs in range(bugs_per_line, b + 1):
                cur[bugs] = (cur[bugs] + prev[bugs - bugs_per_line]) % mod

    print(sum(dp[m]) % mod)

if __name__ == "__main__":
    main()
