import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    cases = []
    pos = 1
    for _ in range(q):
        cases.append((data[pos].decode(), data[pos + 1].decode()))
        pos += 2
    return cases

# Clause can_type [Confidence: 1.00]
def can_type(s, t):
    i = len(s) - 1
    j = len(t) - 1
    while i >= 0 and j >= 0:
        if s[i] == t[j]:
            i -= 1
            j -= 1
        else:
            i -= 2
    return j < 0

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s, t in read_input():
        out.append("YES" if can_type(s, t) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

