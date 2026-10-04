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

# Clause build_partition [Confidence: 1.00]
def build_partition(a):
    n = len(a)
    if n % 2:
        return None
    pieces = []
    for i in range(0, n, 2):
        if a[i] == a[i + 1]:
            pieces.append((i + 1, i + 2))
        else:
            pieces.append((i + 1, i + 1))
            pieces.append((i + 2, i + 2))
    return pieces

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        pieces = build_partition(a)
        if pieces is None:
            out.append("-1")
            continue
        out.append(str(len(pieces)))
        for bottom, high in pieces:
            out.append("%d %d" % (bottom, high))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

