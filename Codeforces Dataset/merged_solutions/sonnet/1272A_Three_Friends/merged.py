import sys

# Clause read_input [Confidence: 0.80]
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    return [(int(data[3 * i + 1]), int(data[3 * i + 2]), int(data[3 * i + 3]))
            for i in range(q)]

# Clause closest_total [Confidence: 0.80]
def closest_total(a, b, c):
    low = a
    high = a
    for value in (b, c):
        if value < low:
            low = value
        if value > high:
            high = value
    spread = high - low - 2
    if spread < 0:
        spread = 0
    return 2 * spread

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a, b, c in read_input():
        out.append(str(closest_total(a, b, c)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

