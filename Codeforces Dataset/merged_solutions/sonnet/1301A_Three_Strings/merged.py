import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append((data[1 + 3 * i].decode(), data[2 + 3 * i].decode(), data[3 + 3 * i].decode()))
    return cases

# Clause can_match [Confidence: 1.00]
def can_match(a, b, c):
    for i in range(len(c)):
        if c[i] != a[i] and c[i] != b[i]:
            return False
    return True

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for a, b, c in read_input():
        collected.append("YES" if can_match(a, b, c) else "NO")
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

