import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(t)]

# Clause kth_free [Confidence: 0.60]
def kth_free(n, k):
    return k + (k - 1) // (n - 1)

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, k in read_input():
        out.append(str(kth_free(n, k)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

