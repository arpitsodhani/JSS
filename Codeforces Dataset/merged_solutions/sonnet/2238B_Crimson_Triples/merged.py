import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(data[1 + i]) for i in range(t)]

# Clause count_triples [Confidence: 0.60]
def count_triples(n):
    total = 0
    for b in range(1, n + 1):
        share = n // b
        total += share * share
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        out.append(str(count_triples(n)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

