import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[2 * i + 2] for i in range(t)]

# Clause spread_letters [Confidence: 0.60]
def spread_letters(s):
    counts = [0] * 26
    for ch in s:
        counts[ch - 97] += 1
    out = []
    left = len(s)
    while left:
        for k in range(26):
            if counts[k]:
                out.append(chr(97 + k))
                counts[k] -= 1
                left -= 1
    return "".join(out)

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s in read_input():
        out.append(spread_letters(s))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

