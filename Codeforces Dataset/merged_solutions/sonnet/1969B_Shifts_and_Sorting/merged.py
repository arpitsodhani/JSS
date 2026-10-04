import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i] for i in range(t)]

# Clause sorting_cost [Confidence: 1.00]
def sorting_cost(s):
    ones = 0
    total = 0
    for ch in s:
        if ch == 49:
            ones += 1
        elif ones > 0:
            total += ones + 1
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s in read_input():
        out.append(str(sorting_cost(s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

