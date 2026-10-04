import sys

# Clause read_input [Confidence: 0.80]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(v) for v in data[1:t + 1]]

# Clause build_triple [Confidence: 0.60]
def build_triple(n):
    if n & 1:
        return "-1"
    half = n >> 1
    return "%d %d 0" % (half, half)

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        out.append(build_triple(n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

