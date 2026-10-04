import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# Clause count_pairs [Confidence: 0.80]
def count_pairs(s, x):
    if s < x or (s - x) % 2:
        return 0
    carry = (s - x) // 2
    if carry & x:
        return 0
    total = 1 << bin(x).count("1")
    if carry == 0:
        total -= 2
    return total if total > 0 else 0

# Clause main [Confidence: 1.00]
def main():
    s, x = read_input()
    sys.stdout.write(str(count_pairs(s, x)) + "\n")


if __name__ == "__main__":
    main()

