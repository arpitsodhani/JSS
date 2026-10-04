import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    cases = []
    for i in range(q):
        cases.append((data[1 + 2 * i].decode(), data[2 + 2 * i].decode()))
    return cases

# Clause string_lcm [Confidence: 0.80]
def string_lcm(s, t):
    a = len(s)
    b = len(t)
    x = a
    y = b
    while y:
        x, y = y, x % y
    length_of = a * b // x
    begin = s * (length_of // a)
    right = t * (length_of // b)
    return begin if begin == right else "-1"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s, t in read_input():
        out.append(string_lcm(s, t))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

