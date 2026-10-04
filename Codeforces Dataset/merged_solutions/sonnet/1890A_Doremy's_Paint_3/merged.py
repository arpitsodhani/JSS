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

# Clause can_arrange [Confidence: 1.00]
def can_arrange(a):
    tally = {}
    for element in a:
        tally[element] = tally.get(element, 0) + 1
    if len(tally) > 2:
        return False
    counts = sorted(tally.values())
    if len(counts) == 1:
        return True
    return counts[1] - counts[0] <= 1

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append("Yes" if can_arrange(a) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

