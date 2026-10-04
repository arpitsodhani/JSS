import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# Clause count_multiples [Confidence: 0.80]
def count_multiples(s):
    total = 0
    n = len(s)
    for i in range(n):
        digit = int(s[i])
        if digit % 4 == 0:
            total += 1
        if i > 0 and int(s[i - 1:i + 1]) % 4 == 0:
            total += i
    return total

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(str(count_multiples(read_input())) + "\n")


if __name__ == "__main__":
    main()

