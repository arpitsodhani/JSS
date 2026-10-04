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

# Clause doom_year [Confidence: 0.80]
def doom_year(signs):
    year = 0
    for jump in signs:
        year = (year // jump + 1) * jump
    return year

# Clause main [Confidence: 1.00]
def main():
    out = []
    for signs in read_input():
        out.append(doom_year(signs))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

