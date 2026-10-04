# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    values = list(map(int, sys.stdin.read().split()))
    if not values:
        return
    counts = {}
    pairs = 0
    for length in values[1:values[0] + 1]:
        current = counts.get(length, 0) + 1
        if current == 2:
            pairs += 1
            current = 0
        counts[length] = current


# Clause finish_program [Confidence: 0.60]
    print(pairs // 2)

if __name__ == "__main__":
    main()


