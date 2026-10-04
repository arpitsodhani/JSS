import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause undo_layers [Confidence: 1.00]
def undo_layers(a):
    band = list(a)
    n = len(band)
    for i in range(0, n // 2, 2):
        j = n - 1 - i
        band[i], band[j] = band[j], band[i]
    return band

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(" ".join(map(str, undo_layers(read_input()))) + "\n")


if __name__ == "__main__":
    main()

