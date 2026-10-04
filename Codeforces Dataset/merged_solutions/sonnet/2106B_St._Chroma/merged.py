import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        x = int(data[pos + 1])
        pos += 2
        cases.append((n, x))
    return cases

# Clause build_permutation [Confidence: 1.00]
def build_permutation(n, x):
    if n == x:
        return list(range(n))
    order = list(range(x))
    order.extend(range(x + 1, n))
    order.append(x)
    return order

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, x in read_input():
        out.append(" ".join(map(str, build_permutation(n, x))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

