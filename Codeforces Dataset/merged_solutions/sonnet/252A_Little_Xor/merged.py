import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:n + 1]))
    return n, values

# Clause best_xor [Confidence: 0.80]
def best_xor(n, values):
    best = 0
    for start in range(n):
        running = 0
        for end in range(start, n):
            running ^= values[end]
            if running > best:
                best = running
    return best

# Clause main [Confidence: 1.00]
def main():
    n, values = read_input()
    sys.stdout.write(str(best_xor(n, values)) + "\n")


if __name__ == "__main__":
    main()

