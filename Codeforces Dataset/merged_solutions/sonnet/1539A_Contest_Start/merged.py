import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    k = data[0]
    cases = []
    pos = 1
    for _ in range(k):
        cases.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return cases

# Clause total_dissatisfaction [Confidence: 1.00]
def total_dissatisfaction(n, x, t):
    reach = t // x
    if reach >= n:
        return n * (n - 1) // 2
    return (n - reach) * reach + reach * (reach - 1) // 2

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, x, t in read_input():
        out.append(str(total_dissatisfaction(n, x, t)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

