import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]

# Clause count_marks [Confidence: 0.80]
def count_marks(s):
    amount = 0
    run = 0
    for ch in s:
        if ch == "v":
            run += 1
        else:
            amount += run // 2 + 1
            run = 0
    amount += run // 2
    return amount

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for s in read_input():
        lines.append(count_marks(s))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()

