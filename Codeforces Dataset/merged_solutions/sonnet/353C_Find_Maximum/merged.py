import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = [int(data[1 + i]) for i in range(n)]
    return a, data[1 + n].decode()

# Clause best_value [Confidence: 1.00]
def best_value(a, bits):
    n = len(a)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    best = 0
    running = 0
    for level in range(n - 1, -1, -1):
        if bits[level] == "1":
            here = running + prefix[level]
            if here > best:
                best = here
            running += a[level]
    if running > best:
        best = running
    return best

# Clause main [Confidence: 1.00]
def main():
    a, bits = read_input()
    sys.stdout.write("%d\n" % best_value(a, bits))


if __name__ == "__main__":
    main()

