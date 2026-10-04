# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.50]
def main():
    n = int(sys.stdin.readline())
    ans = 0
    while n:
        text = str(n)
        digit = max(map(int, text))
        if digit == 9:
            idx = text.rfind("9")
            tail_len = len(text) - idx - 1
            unit = 10 ** tail_len
            steps = (n % unit) // 9 + 1
        else:
            steps = 1
        n -= digit * steps
        ans += steps


# Clause finish_program [Confidence: 0.50]
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    main()


