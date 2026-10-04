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
        l = data[pos:pos + n]
        pos += n
        r = data[pos:pos + n]
        pos += n
        c = data[pos:pos + n]
        pos += n
        cases.append((l, r, c))
    return cases

# Clause match_lengths [Confidence: 0.80]
def match_lengths(l, r):
    events = []
    for element in l:
        events.append((element, 0))
    for element in r:
        events.append((element, 1))
    events.sort()
    stack = []
    lengths = []
    for element, kind in events:
        if kind == 0:
            stack.append(element)
        else:
            lengths.append(element - stack.pop())
    return lengths

# Clause least_weight [Confidence: 1.00]
def least_weight(lengths, c):
    lengths.sort()
    costs = sorted(c, reverse=True)
    total = 0
    for i in range(len(lengths)):
        total += lengths[i] * costs[i]
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for l, r, c in read_input():
        out.append(least_weight(match_lengths(l, r), c))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

