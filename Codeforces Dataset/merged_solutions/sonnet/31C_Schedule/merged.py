import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]

# Clause find_clash [Confidence: 1.00]
def find_clash(groups, skip):
    arranged = []
    for i in range(len(groups)):
        if i != skip:
            arranged.append((groups[i][0], groups[i][1], i))
    arranged.sort()
    for j in range(1, len(arranged)):
        if arranged[j][0] < arranged[j - 1][1]:
            return arranged[j - 1][2], arranged[j][2]
    return -1, -1

# Clause droppable [Confidence: 1.00]
def droppable(groups):
    a, b = find_clash(groups, -1)
    if a < 0:
        return [i + 1 for i in range(len(groups))]
    lines = []
    for skip in (a, b):
        if find_clash(groups, skip)[0] < 0:
            lines.append(skip + 1)
    lines.sort()
    return lines

# Clause main [Confidence: 1.00]
def main():
    lines = droppable(read_input())
    sys.stdout.write("%d\n%s\n" % (len(lines), " ".join(map(str, lines))))


if __name__ == "__main__":
    main()

