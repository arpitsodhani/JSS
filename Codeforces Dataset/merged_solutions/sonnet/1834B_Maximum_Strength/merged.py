import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos].decode(), data[pos + 1].decode()))
        pos += 2
    return cases

# Clause best_strength [Confidence: 0.80]
def best_strength(low, high):
    width = len(high)
    padded = low.rjust(width, "0")
    for i in range(width):
        if padded[i] != high[i]:
            return (int(high[i]) - int(padded[i])) + 9 * (width - i - 1)
    return 0

# Clause main [Confidence: 1.00]
def main():
    out = []
    for low, high in read_input():
        out.append(str(best_strength(low, high)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

