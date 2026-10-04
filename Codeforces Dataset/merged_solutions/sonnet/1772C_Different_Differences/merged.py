import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause build_row [Confidence: 0.80]
def build_row(k, n):
    row = [1]
    jump = 1
    while len(row) < k:
        nxt = row[-1] + jump
        begin = k - len(row) - 1
        if nxt + begin <= n:
            row.append(nxt)
            jump += 1
        else:
            row.append(row[-1] + 1)
    return row

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, n in read_input():
        out.append(" ".join(map(str, build_row(k, n))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

