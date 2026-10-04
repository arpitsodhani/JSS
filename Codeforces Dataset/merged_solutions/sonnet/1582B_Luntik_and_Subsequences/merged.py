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

# Clause count_subsequences [Confidence: 0.80]
def count_subsequences(a):
    zeros = 0
    ones = 0
    for element in a:
        if element == 0:
            zeros += 1
        elif element == 1:
            ones += 1
    return ones * (1 << zeros)

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(count_subsequences(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

