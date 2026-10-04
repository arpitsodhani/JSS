import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])

# Clause best_prize [Confidence: 0.80]
def best_prize(n):
    total = 0.0
    for opponents in range(1, n + 1):
        total += 1.0 / opponents
    return total

# Clause main [Confidence: 1.00]
def main():
    n = read_input()
    sys.stdout.write("%.12f\n" % best_prize(n))


if __name__ == "__main__":
    main()

