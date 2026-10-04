import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    correct = data[2:2 + n]
    wrong = data[2 + n:2 + n + m]
    return correct, wrong

# Clause best_limit [Confidence: 0.40]
def best_limit(correct, wrong):
    limit = max(max(correct), 2 * min(correct))
    if limit < min(wrong):
        return limit
    return -1

# Clause main [Confidence: 1.00]
def main():
    correct, wrong = read_input()
    sys.stdout.write(str(best_limit(correct, wrong)) + "\n")


if __name__ == "__main__":
    main()

