# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    parts = list(map(int, sys.stdin.read().split()))
    bars = parts[1:]
    unique_lengths = set(bars)
    tallest = 0
    for length in unique_lengths:
        amount = bars.count(length)
        if amount > tallest:
            tallest = amount


# Clause finish_program [Confidence: 0.40]
    print(best, different)

if __name__ == "__main__":
    main()


