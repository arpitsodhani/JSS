import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        s = data[pos + 1]
        pos += 2
        cases.append((n, s, data[pos:pos + n]))
        pos += n
    return cases

# Clause rearrange [Confidence: 0.80]
def rearrange(n, s, a):
    total = sum(a)
    if s == total or s > total + 1:
        return None
    zeros = a.count(0)
    ones = a.count(1)
    twos = n - zeros - ones
    return [0] * zeros + [2] * twos + [1] * ones

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, s, a in read_input():
        order = rearrange(n, s, a)
        if order is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, order)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

