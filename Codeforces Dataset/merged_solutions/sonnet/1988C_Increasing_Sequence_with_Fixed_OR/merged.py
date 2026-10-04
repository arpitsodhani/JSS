import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause build_sequence [Confidence: 1.00]
def build_sequence(n):
    bits = []
    element = n
    while element:
        small = element & (-element)
        bits.append(small)
        element -= small
    if len(bits) == 1:
        return [n]
    steps = sorted(n - bit for bit in bits)
    steps.append(n)
    return steps

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        steps = build_sequence(n)
        out.append(str(len(steps)))
        out.append(" ".join(map(str, steps)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

