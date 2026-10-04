import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    cases = []
    pos = 1
    for _ in range(q):
        pos += 1
        cases.append(data[pos].decode())
        pos += 1
    return cases

# Clause split_digits [Confidence: 0.40]
def split_digits(s):
    if len(s) > 2 or s[0] < s[1]:
        return [s[0], s[1:]]
    return None

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s in read_input():
        parts = split_digits(s)
        if parts is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append(str(len(parts)))
            out.append(" ".join(parts))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

