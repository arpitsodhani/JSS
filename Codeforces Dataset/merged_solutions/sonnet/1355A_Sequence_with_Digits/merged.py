import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause run_sequence [Confidence: 0.80]
def run_sequence(start, k):
    entry = start
    for _ in range(k - 1):
        low = 9
        upper = 0
        rest = entry
        while rest:
            digit = rest % 10
            if digit < low:
                low = digit
            if digit > upper:
                upper = digit
            rest //= 10
        if low == 0:
            break
        entry += low * upper
    return entry

# Clause main [Confidence: 1.00]
def main():
    out = []
    for start, k in read_input():
        out.append(run_sequence(start, k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

