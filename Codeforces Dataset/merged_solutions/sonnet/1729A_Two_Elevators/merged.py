import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]))
    return cases

# Clause better_elevator [Confidence: 1.00]
def better_elevator(a, b, c):
    first = a - 1
    follow = abs(b - c) + c - 1
    if first < follow:
        return 1
    if follow < first:
        return 2
    return 3

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a, b, c in read_input():
        out.append(better_elevator(a, b, c))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

