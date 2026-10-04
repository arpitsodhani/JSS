import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause digit_sum [Confidence: 1.00]
def digit_sum(value):
    amount = 0
    while value:
        amount += value % 10
        value //= 10
    return amount

# Clause perfect_number [Confidence: 1.00]
def perfect_number(k):
    discovered = 0
    value = 19
    while True:
        if digit_sum(value) == 10:
            discovered += 1
            if discovered == k:
                return value
        value += 9
    return -1

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % perfect_number(read_input()))


if __name__ == "__main__":
    main()

