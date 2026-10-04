import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause digit_sum [Confidence: 1.00]
def digit_sum(n):
    amount = 0
    while n:
        amount += n % 10
        n //= 10
    return amount

# Clause moves_needed [Confidence: 1.00]
def moves_needed(n, s):
    power = 1
    entry = n
    while digit_sum(entry) > s:
        power *= 10
        entry = (n // power + 1) * power
    return entry - n

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, s in read_input():
        out.append(moves_needed(n, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

