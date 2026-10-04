# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.40]
def value(n):
    blocked = {0}
    if n == 1:
        return 1
    return 0 if n % 2 in blocked or n % 3 in blocked else 1

def main():
    items = list(map(int, sys.stdin.read().split()))
    if len(items) == 0:
        return
    print(value(items[0]))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


