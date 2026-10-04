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

# Clause count_triangles [Confidence: 0.80]
def count_triangles(a):
    n = len(a)
    counts = [0] * (n + 1)
    for value in a:
        counts[value] += 1
    total = 0
    smaller = 0
    for c in counts:
        if c >= 3:
            total += c * (c - 1) * (c - 2) // 6
        if c >= 2 and smaller:
            total += c * (c - 1) // 2 * smaller
        smaller += c
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(str(count_triangles(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

