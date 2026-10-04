import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[2 * i + 2] for i in range(t)]

# Clause countdown_cost [Confidence: 0.80]
def countdown_cost(digits):
    total = 0
    nonzero = 0
    for ch in digits:
        value = ch - 48
        total += value
        if value:
            nonzero += 1
    if nonzero and digits[len(digits) - 1] != 48:
        nonzero -= 1
    return total + nonzero

# Clause main [Confidence: 1.00]
def main():
    out = []
    for digits in read_input():
        out.append(str(countdown_cost(digits)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

