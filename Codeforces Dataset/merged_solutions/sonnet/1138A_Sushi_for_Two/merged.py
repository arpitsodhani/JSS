# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    sushi = data[1:1 + n]
    runs = []
    current = sushi[0]
    count = 0
    for value in sushi:
        if value == current:
            count += 1
        else:
            runs.append(count)
            current = value
            count = 1
    runs.append(count)
    best = 0
    for left, right in zip(runs, runs[1:]):
        length = 2 * min(left, right)
        if length > best:
            best = length
    sys.stdout.write(str(best))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


