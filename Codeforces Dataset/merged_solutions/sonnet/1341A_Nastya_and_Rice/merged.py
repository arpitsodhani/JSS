import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    return [tuple(data[1 + 5 * i:6 + 5 * i]) for i in range(t)]

# Clause is_possible [Confidence: 1.00]
def is_possible(n, a, b, c, d):
    bottom = n * (a - b)
    high = n * (a + b)
    return bottom <= c + d and c - d <= high

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, a, b, c, d in read_input():
        out.append("Yes" if is_possible(n, a, b, c, d) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

