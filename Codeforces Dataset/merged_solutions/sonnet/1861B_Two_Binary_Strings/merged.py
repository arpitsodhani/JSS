import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i].decode(), data[2 + 2 * i].decode()))
    return cases

# Clause can_match [Confidence: 1.00]
def can_match(a, b):
    for i in range(len(a) - 1):
        if a[i] == "0" and b[i] == "0" and a[i + 1] == "1" and b[i + 1] == "1":
            return True
    return False

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for a, b in read_input():
        collected.append("YES" if can_match(a, b) else "NO")
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

