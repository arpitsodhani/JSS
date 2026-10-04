import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(token) for token in data[1:n + 1]]
    return n, values

# Clause split_sets [Confidence: 0.80]
def split_sets(n, values):
    negatives = []
    positives = []
    zeros = []
    for value in values:
        if value < 0:
            negatives.append(value)
        elif value > 0:
            positives.append(value)
        else:
            zeros.append(value)
    first = [negatives[0]]
    rest = negatives[1:]
    if len(rest) % 2 == 1:
        zeros.append(rest[-1])
        rest = rest[:-1]
    second = positives + rest
    return first, second, zeros

# Clause main [Confidence: 1.00]
def main():
    n, values = read_input()
    first, second, zeros = split_sets(n, values)
    out = []
    for group in (first, second, zeros):
        out.append(str(len(group)) + " " + " ".join(map(str, group)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

