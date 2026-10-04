import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])

# Clause best_product [Confidence: 0.80]
def best_product(n):
    if n == 0:
        return 1
    if n < 10:
        return n
    keep = (n % 10) * best_product(n // 10)
    drop = 9 * best_product(n // 10 - 1)
    if keep > drop:
        return keep
    return drop

# Clause main [Confidence: 1.00]
def main():
    n = read_input()
    sys.stdout.write(str(best_product(n)) + "\n")


if __name__ == "__main__":
    main()

