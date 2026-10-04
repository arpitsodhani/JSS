import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        x = data[pos + 1]
        pos += 2
        cases.append((x, data[pos:pos + n]))
        pos += n
    return cases

# Clause beauty_range [Confidence: 0.80]
def beauty_range(x, a):
    total = 0
    spread = 0
    for element in a:
        total += element
        spread += (element + x - 1) // x
    return (total + x - 1) // x, spread

# Clause main [Confidence: 1.00]
def main():
    out = []
    for x, a in read_input():
        out.append("%d %d" % beauty_range(x, a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

