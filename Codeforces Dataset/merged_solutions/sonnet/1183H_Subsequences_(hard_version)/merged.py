# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]

    dp = [0] * (n + 1)
    dp[0] = 1
    last = [[0] * (n + 1) for _ in range(26)]

    for i, ch in enumerate(s, 1):
        c = ord(ch) - 97
        for length in range(i, 0, -1):
            old = dp[length - 1]
            dp[length] += old - last[c][length]
            last[c][length] = old

    need = k
    total = 0
    for length in range(n, -1, -1):
        used = min(need, dp[length])
        total += used * (n - length)
        need -= used
        if need == 0:
            sys.stdout.write(str(total))
            return
    sys.stdout.write("-1")


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


