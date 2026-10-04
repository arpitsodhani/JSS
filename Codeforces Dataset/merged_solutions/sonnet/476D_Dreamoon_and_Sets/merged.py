import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1])

# Clause build_sets [Confidence: 1.00]
def build_sets(n, k):
    out = []
    for i in range(n):
        base = 6 * i + 1
        picks = (base, base + 1, base + 2, base + 4)
        out.append(" ".join(str(k * value) for value in picks))
    return out

# Clause main [Confidence: 1.00]
def main():
    n, k = read_input()
    lines = [str(k * (6 * n - 1))]
    lines.extend(build_sets(n, k))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

