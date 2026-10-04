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

# Clause waiting_time [Confidence: 1.00]
def waiting_time(k, m):
    block = m // k
    rest = block % 3
    if rest == 2:
        return 0
    return (block + 2 - rest) * k - m

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, m in read_input():
        out.append(str(waiting_time(k, m)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

