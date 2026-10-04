import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1]))
        pos += 2
    return cases

# Clause final_position [Confidence: 0.60]
def final_position(start, n):
    skipped = n - n % 4
    position = start
    for jump in range(skipped + 1, n + 1):
        if position % 2 == 0:
            position -= jump
        else:
            position += jump
    return position

# Clause main [Confidence: 1.00]
def main():
    out = []
    for start, n in read_input():
        out.append(str(final_position(start, n)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

