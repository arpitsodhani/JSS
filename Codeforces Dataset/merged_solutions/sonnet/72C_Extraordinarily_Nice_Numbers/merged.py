import sys

# Clause read_input [Confidence: 0.60]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])

# Clause count_divisors [Confidence: 1.00]
def count_divisors(x):
    even = 0
    odd = 0
    for d in range(1, x + 1):
        if x % d == 0:
            if d % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd

# Clause verdict [Confidence: 1.00]
def verdict(even, odd):
    if even == odd:
        return "yes"
    return "no"

# Clause main [Confidence: 0.40]
def main():
    x = read_input()
    even, odd = count_divisors(x)
    sys.stdout.write(verdict(even, odd) + "\n")


if __name__ == "__main__":
    main()

