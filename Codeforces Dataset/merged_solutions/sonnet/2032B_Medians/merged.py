import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1]))
        pos += 2
    return cases

# Clause split_points [Confidence: 0.60]
def split_points(n, k):
    if n == 1:
        return [1] if k == 1 else None
    if k == 1 or k == n:
        return None
    if k % 2 == 0:
        return [1, k, k + 1]
    return [1, k - 1, k + 2]

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, k in read_input():
        starts = split_points(n, k)
        if starts is None:
            out.append("-1")
        else:
            out.append(str(len(starts)))
            out.append(" ".join(map(str, starts)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

