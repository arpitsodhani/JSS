# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    if n == 1:
        result = 1
    else:
        result = 3 * n * n - n - 1
        if n >= 3:
            result = max(result, 5 * (n * n - n - 1))
            result = max(result, 4 * (n * n - 1) - n)
    print(result)


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


