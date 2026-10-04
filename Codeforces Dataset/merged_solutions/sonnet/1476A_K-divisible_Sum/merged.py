import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause smallest_peak [Confidence: 0.80]
def smallest_peak(n, k):
    amount = ((n + k - 1) // k) * k
    return (amount + n - 1) // n

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for n, k in read_input():
        lines.append(smallest_peak(n, k))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()

