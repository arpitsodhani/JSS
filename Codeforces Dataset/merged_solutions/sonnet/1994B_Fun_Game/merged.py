import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    pos = 1
    cases = []
    for _ in range(q):
        s = data[pos + 1].decode()
        t = data[pos + 2].decode()
        pos += 3
        cases.append((s, t))
    return cases

# Clause first_one [Confidence: 1.00]
def first_one(bits):
    for i in range(len(bits)):
        if bits[i] == "1":
            return i
    return len(bits)

# Clause is_interesting [Confidence: 0.80]
def is_interesting(s, t):
    return first_one(s) <= first_one(t)

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for s, t in read_input():
        lines.append("YES" if is_interesting(s, t) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

