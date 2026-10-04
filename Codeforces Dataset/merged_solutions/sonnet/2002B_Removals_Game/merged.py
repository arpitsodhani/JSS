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
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
        cases.append((a, b))
    return cases

# Clause solve_case [Confidence: 0.40]
def solve_case(a, b):
    if a == b:
        return "Bob"
    if a == b[::-1]:
        return "Bob"
    return "Alice"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a, b in read_input():
        out.append(solve_case(a, b))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

