import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return cases

# Clause eggs_needed [Confidence: 0.60]
def eggs_needed(n, s, t):
    without_sticker = n - s
    without_toy = n - t
    worst = without_sticker if without_sticker > without_toy else without_toy
    return worst + 1

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, s, t in read_input():
        out.append(str(eggs_needed(n, s, t)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

