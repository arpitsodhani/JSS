import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1]), int(data[2]), int(data[3])

# Clause gcd_of [Confidence: 1.00]
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a

# Clause candidate_lengths [Confidence: 1.00]
def candidate_lengths(n, k, a, b):
    bases = set()
    for base in (b - a, b + a, -a - b, a - b):
        bases.add(base % k)
    amount = n * k
    lengths = []
    for base in bases:
        for i in range(n + 1):
            advance = base + i * k
            if 0 < advance <= amount:
                lengths.append(advance)
    return lengths

# Clause stop_range [Confidence: 1.00]
def stop_range(n, k, lengths):
    amount = n * k
    low = amount
    high = 1
    for advance in lengths:
        stops = amount // gcd_of(amount, advance)
        if stops < low:
            low = stops
        if stops > high:
            high = stops
    return low, high

# Clause main [Confidence: 1.00]
def main():
    n, k, a, b = read_input()
    lengths = candidate_lengths(n, k, a, b)
    low, high = stop_range(n, k, lengths)
    sys.stdout.write("%d %d\n" % (low, high))


if __name__ == "__main__":
    main()

