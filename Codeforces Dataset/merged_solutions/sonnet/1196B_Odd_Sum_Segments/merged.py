import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    q = int(data[pos])
    pos += 1
    cases = []
    for _ in range(q):
        n = int(data[pos])
        k = int(data[pos + 1])
        pos += 2
        values = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, k, values))
    return cases

# Clause split_points [Confidence: 1.00]
def split_points(n, k, values):
    spots = []
    for i in range(n):
        if values[i] % 2:
            spots.append(i + 1)
    if len(spots) < k or (len(spots) - k) % 2:
        return None
    cuts = spots[:k - 1]
    cuts.append(n)
    return cuts

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, k, values in read_input():
        cuts = split_points(n, k, values)
        if cuts is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append(" ".join(map(str, cuts)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

