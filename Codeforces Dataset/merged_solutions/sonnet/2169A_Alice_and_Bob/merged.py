import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        a = int(data[pos + 1])
        pos += 2
        marbles = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((a, marbles))
    return cases

# Clause pick_number [Confidence: 0.40]
def pick_number(a, marbles):
    above = 0
    below = 0
    for value in marbles:
        if value > a:
            above += 1
        elif value < a:
            below += 1
    if below > above:
        return a - 1
    return a + 1

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a, marbles in read_input():
        out.append(str(pick_number(a, marbles)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

