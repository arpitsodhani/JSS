import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        target = data[pos + 1]
        pos += 2
        cases.append((target, data[pos:pos + n]))
        pos += n
    return cases

# Clause paint [Confidence: 0.80]
def paint(target, a):
    colours = []
    swing = 0
    for entry in a:
        if 2 * entry < target:
            colours.append(0)
        elif 2 * entry > target:
            colours.append(1)
        else:
            colours.append(swing)
            swing = 1 - swing
    return colours

# Clause main [Confidence: 1.00]
def main():
    out = []
    for target, a in read_input():
        out.append(" ".join(map(str, paint(target, a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

