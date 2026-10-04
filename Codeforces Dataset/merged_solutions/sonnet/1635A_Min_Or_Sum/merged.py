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

# Clause smallest_sum [Confidence: 0.60]
def smallest_sum(a):
    bits = 0
    for value in a:
        bits |= value
    return bits

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(str(smallest_sum(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

