import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[2:2 + data[0]]

# Clause colour_order [Confidence: 1.00]
def colour_order(colours):
    tally = {}
    for element in colours:
        tally[element] = tally.get(element, 0) + 1
    ranked = sorted(tally, key=lambda element: (-tally[element], element))
    line = []
    for element in ranked:
        for _ in range(tally[element]):
            line.append(element)
    return line

# Clause pair_up [Confidence: 0.80]
def pair_up(line):
    n = len(line)
    shift = n // 2
    rights = line[shift:] + line[:shift]
    good = []
    bad = []
    for i in range(n):
        if line[i] != rights[i]:
            good.append((line[i], rights[i]))
        else:
            bad.append((line[i], rights[i]))
    return len(good), good + bad

# Clause main [Confidence: 1.00]
def main():
    colours = read_input()
    count, pairs = pair_up(colour_order(colours))
    out = [str(count)]
    for left, right in pairs:
        out.append("%d %d" % (left, right))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

