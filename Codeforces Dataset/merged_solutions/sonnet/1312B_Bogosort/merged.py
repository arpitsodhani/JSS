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

# Clause good_order [Confidence: 0.80]
def good_order(a):
    return sorted(a, reverse=True)

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for a in read_input():
        lines.append(" ".join(map(str, good_order(a))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

