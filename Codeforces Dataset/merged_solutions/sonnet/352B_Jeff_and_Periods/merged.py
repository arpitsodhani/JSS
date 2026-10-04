import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]

# Clause arithmetic_values [Confidence: 0.80]
def arithmetic_values(n, a):
    last = {}
    step = {}
    good = {}
    for index, value in enumerate(a):
        if value not in last:
            last[value] = index
            step[value] = 0
            good[value] = True
            continue
        gap = index - last[value]
        if step[value] == 0:
            step[value] = gap
        elif step[value] != gap:
            good[value] = False
        last[value] = index
    out = []
    for value in sorted(good):
        if good[value]:
            out.append((value, step[value]))
    return out

# Clause main [Confidence: 1.00]
def main():
    n, a = read_input()
    found = arithmetic_values(n, a)
    lines = [str(len(found))]
    for value, gap in found:
        lines.append("%d %d" % (value, gap))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

