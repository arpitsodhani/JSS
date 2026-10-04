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

# Clause cheapest_cover [Confidence: 0.80]
def cheapest_cover(a, b):
    n = len(a)
    rows = min(a) * n + sum(b)
    columns = min(b) * n + sum(a)
    return rows if rows < columns else columns

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for a, b in read_input():
        lines.append(cheapest_cover(a, b))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()

