import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(data[1 + i]) for i in range(t)]

# Clause build_sequence [Confidence: 0.80]
def build_sequence(n):
    values = [3 * n, 5 * n]
    middle = n - 2
    if middle % 2 == 0:
        half = middle // 2
        for step in range(1, half + 1):
            values.append(4 * n - step)
            values.append(4 * n + step)
    else:
        values.append(4 * n)
        half = (middle - 1) // 2
        for step in range(1, half + 1):
            values.append(4 * n - step)
            values.append(4 * n + step)
    return values

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        out.append(" ".join(map(str, build_sequence(n))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

