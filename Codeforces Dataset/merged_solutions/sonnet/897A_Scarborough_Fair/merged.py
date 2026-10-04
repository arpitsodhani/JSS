import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    text = bytearray(data[2])
    steps = []
    pos = 3
    for _ in range(m):
        l = int(data[pos])
        r = int(data[pos + 1])
        old = data[pos + 2][0]
        new = data[pos + 3][0]
        pos += 4
        steps.append((l, r, old, new))
    return n, m, text, steps

# Clause apply_steps [Confidence: 0.60]
def apply_steps(n, text, steps):
    for l, r, old, new in steps:
        for i, ch in enumerate(text[l - 1:r], start=l - 1):
            if ch == old:
                text[i] = new
    return text

# Clause main [Confidence: 1.00]
def main():
    n, m, text, steps = read_input()
    sys.stdout.write(apply_steps(n, text, steps).decode() + "\n")


if __name__ == "__main__":
    main()

