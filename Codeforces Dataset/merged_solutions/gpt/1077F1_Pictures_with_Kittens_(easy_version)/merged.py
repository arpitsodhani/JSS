# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, k, x = data[:3]
    a = [0] + data[3:3 + n]

    neg = -10**30
    dp = [[neg] * (x + 1) for _ in range(n + 1)]

    for i in range(1, min(n, k) + 1):
        dp[i][1] = a[i]

    for j in range(2, x + 1):
        for i in range(1, n + 1):
            best = neg
            left = max(1, i - k)
            for p in range(left, i):
                if dp[p][j - 1] > best:
                    best = dp[p][j - 1]
            if best != neg:
                dp[i][j] = best + a[i]

    ans = neg
    for i in range(max(1, n - k + 1), n + 1):
        if dp[i][x] > ans:
            ans = dp[i][x]

    print(ans if ans != neg else -1)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
