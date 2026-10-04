import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause three_parts [Confidence: 1.00]
def three_parts(n):
    if n % 2:
        return 1, (n - 1) // 2, (n - 1) // 2
    if n % 4 == 0:
        return n // 2, n // 4, n // 4
    return 2, (n - 2) // 2, (n - 2) // 2

# Clause split_parts [Confidence: 1.00]
def split_parts(n, k):
    parts = [1] * (k - 3)
    return parts + list(three_parts(n - (k - 3)))

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n, k in read_input():
        collected.append(" ".join(map(str, split_parts(n, k))))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

