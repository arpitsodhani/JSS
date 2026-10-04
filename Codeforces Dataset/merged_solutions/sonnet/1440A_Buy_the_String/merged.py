import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        c0 = int(data[pos + 1])
        c1 = int(data[pos + 2])
        h = int(data[pos + 3])
        s = data[pos + 4].decode()
        pos += 5
        cases.append((c0, c1, h, s))
    return cases

# Clause least_price [Confidence: 0.80]
def least_price(c0, c1, h, s):
    zero = c0 if c0 < c1 + h else c1 + h
    one = c1 if c1 < c0 + h else c0 + h
    amount = 0
    for ch in s:
        amount += zero if ch == "0" else one
    return amount

# Clause main [Confidence: 1.00]
def main():
    out = []
    for c0, c1, h, s in read_input():
        out.append(least_price(c0, c1, h, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

