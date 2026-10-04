import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        k = int(data[pos + 1])
        s = data[pos + 2].decode()
        pos += 3
        cases.append((k, s))
    return cases

# Clause can_clear [Confidence: 1.00]
def can_clear(k, s):
    for begin in range(k):
        ones = 0
        for i in range(begin, len(s), k):
            if s[i] == "1":
                ones += 1
        if ones % 2:
            return False
    return True

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, s in read_input():
        out.append("YES" if can_clear(k, s) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

