import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        wants = []
        for _ in range(n):
            wants.append((data[pos], data[pos + 1]))
            pos += 2
        cases.append((m, wants))
    return cases

# Clause most_points [Confidence: 1.00]
def most_points(m, wants):
    amount = 0
    clock = 0
    side = 0
    for moment, want in wants:
        gap = moment - clock
        if (gap - (want ^ side)) % 2:
            gap -= 1
        amount += gap
        clock = moment
        side = want
    return amount + m - clock

# Clause main [Confidence: 1.00]
def main():
    out = []
    for m, wants in read_input():
        out.append(most_points(m, wants))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

