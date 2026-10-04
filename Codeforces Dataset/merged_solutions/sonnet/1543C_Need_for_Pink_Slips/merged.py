import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append((float(data[1 + 4 * i]), float(data[2 + 4 * i]),
                      float(data[3 + 4 * i]), float(data[4 + 4 * i])))
    return cases

# Clause walk [Confidence: 1.00]
def walk(c, m, v, depth):
    eps = 1e-9
    amount = (1.0 - c - m) * depth
    if c > eps:
        others = 2 if m > eps else 1
        if c <= v + eps:
            share = c / others if m > eps else 0.0
            amount += c * walk(0.0, m + share, v, depth + 1)
        else:
            share = v / others if m > eps else 0.0
            amount += c * walk(c - v, m + share, v, depth + 1)
    if m > eps:
        others = 2 if c > eps else 1
        if m <= v + eps:
            share = m / others if c > eps else 0.0
            amount += m * walk(c + share, 0.0, v, depth + 1)
        else:
            share = v / others if c > eps else 0.0
            amount += m * walk(c + share, m - v, v, depth + 1)
    return amount

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for c, m, p, v in read_input():
        lines.append("%.12f" % walk(c, m, v, 1))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

