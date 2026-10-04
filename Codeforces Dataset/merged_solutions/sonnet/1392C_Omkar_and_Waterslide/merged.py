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

# Clause raise_count [Confidence: 0.80]
def raise_count(a):
    amount = 0
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            amount += a[i - 1] - a[i]
    return amount

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(raise_count(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

