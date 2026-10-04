import sys

# Clause read_input [Confidence: 0.60]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        a = int(data[pos])
        b = int(data[pos + 1])
        c = int(data[pos + 2])
        pos += 3
        cases.append((a, b, c))
    return cases

# Clause solve_case [Confidence: 0.60]
def solve_case(a, b, c):
    if (a + b + c) % 3 == 0:
        return 0
    return 1

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a, b, c in read_input():
        out.append(str(solve_case(a, b, c)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

