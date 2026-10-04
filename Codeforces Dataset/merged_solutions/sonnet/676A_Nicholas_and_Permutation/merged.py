import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]

# Clause best_distance [Confidence: 0.40]
def best_distance(n, a):
    low = a.index(1)
    high = a.index(n)
    return max(max(low, high), n - 1 - min(low, high))

# Clause main [Confidence: 1.00]
def main():
    n, a = read_input()
    sys.stdout.write(str(best_distance(n, a)) + "\n")


if __name__ == "__main__":
    main()

