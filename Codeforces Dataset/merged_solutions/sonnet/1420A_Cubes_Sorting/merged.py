import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        cases.append([int(token) for token in data[pos:pos + n]])
        pos += n
    return cases

# Clause can_sort [Confidence: 0.40]
def can_sort(values):
    for i in range(1, len(values)):
        if values[i - 1] <= values[i]:
            return "YES"
    return "NO"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for case in read_input():
        out.append(can_sort(case))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

