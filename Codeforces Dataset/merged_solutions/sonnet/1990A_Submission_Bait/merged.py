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

# Clause alice_wins [Confidence: 0.80]
def alice_wins(a):
    tally = {}
    for entry in a:
        tally[entry] = tally.get(entry, 0) + 1
    for entry in tally:
        if tally[entry] % 2:
            return True
    return False

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append("YES" if alice_wins(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

