import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause coins_needed [Confidence: 1.00]
def coins_needed(a):
    peak = a[0]
    amount = 0
    widest = 0
    for value in a:
        if value > peak:
            peak = value
        gap = peak - value
        amount += gap
        if gap > widest:
            widest = gap
    return amount + widest

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(coins_needed(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

