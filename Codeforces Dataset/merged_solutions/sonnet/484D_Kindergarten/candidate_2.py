import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: best_total :: (n: int, a: list[int]) -> int ---
def best_total(n, a):
    dp = [0] * (n + 1)
    minus = -a[0]
    plus = a[0]
    for i in range(1, n + 1):
        value = a[i - 1]
        dp[i] = max(minus + value, plus - value)
        if i < n:
            following = a[i]
            minus = max(minus, dp[i] - following)
            plus = max(plus, dp[i] + following)
    return dp[n]

# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    sys.stdout.write(str(best_total(n, a)) + "\n")


if __name__ == "__main__":
    main()
