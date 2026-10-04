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

# Clause verdict [Confidence: 1.00]
def verdict(a):
    total = 0
    for entry in a:
        total ^= entry
    if total == 0:
        return "DRAW"
    bit = total.bit_length() - 1
    mine = 0
    for entry in a:
        if (entry >> bit) & 1:
            mine += 1
    rest = len(a) - mine
    if mine % 4 == 1:
        return "WIN"
    return "WIN" if rest % 2 == 1 else "LOSE"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(verdict(a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

