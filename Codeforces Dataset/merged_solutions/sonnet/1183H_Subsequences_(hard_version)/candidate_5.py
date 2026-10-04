# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_counts(n, s):
    dp = [0] * (n + 1)
    dp[0] = 1
    memory = {}

    for used, ch in enumerate(s, 1):
        row = memory.setdefault(ch, [0] * (n + 1))
        for size in range(used, 0, -1):
            before = dp[size - 1]
            dp[size] = dp[size] + before - row[size]
            row[size] = before

    return dp

def choose_best(n, k, counts):
    result = 0
    for size in range(n, -1, -1):
        available = counts[size]
        if k <= available:
            return result + k * (n - size)
        result += available * (n - size)
        k -= available
    return -1

def main():
    raw = sys.stdin.read().split()
    n = int(raw[0])
    k = int(raw[1])
    s = raw[2]
    print(choose_best(n, k, build_counts(n, s)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
