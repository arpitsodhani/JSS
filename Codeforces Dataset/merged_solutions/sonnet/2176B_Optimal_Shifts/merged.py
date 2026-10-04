import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[2 + 2 * i].decode() for i in range(t)]

# Clause widest_gap [Confidence: 0.80]
def widest_gap(s):
    n = len(s)
    spots = []
    for i in range(n):
        if s[i] == "1":
            spots.append(i)
    widest = 0
    for i in range(len(spots)):
        delta = spots[(i + 1) % len(spots)] - spots[i]
        if delta <= 0:
            delta += n
        if delta > widest:
            widest = delta
    return widest - 1

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for s in read_input():
        lines.append(widest_gap(s))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()

