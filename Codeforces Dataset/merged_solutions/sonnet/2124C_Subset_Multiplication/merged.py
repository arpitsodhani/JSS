import sys
from math import gcd

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

# Clause solve_case [Confidence: 1.00]
def solve_case(b):
    x = 1
    for i in range(len(b) - 1):
        need = b[i] // gcd(b[i], b[i + 1])
        x = x * need // gcd(x, need)
    return x

# Clause main [Confidence: 1.00]
def main():
    out = []
    for b in read_input():
        out.append(str(solve_case(b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

