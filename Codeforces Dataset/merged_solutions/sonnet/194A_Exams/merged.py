import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# Clause failed_exams [Confidence: 0.80]
def failed_exams(n, k):
    short = 3 * n - k
    return short if short > 0 else 0

# Clause main [Confidence: 1.00]
def main():
    n, k = read_input()
    sys.stdout.write("%d\n" % failed_exams(n, k))


if __name__ == "__main__":
    main()

