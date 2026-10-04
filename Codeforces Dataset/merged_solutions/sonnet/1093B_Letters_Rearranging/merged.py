import sys

# Clause read_input [Confidence: 0.80]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]

# Clause rearrange [Confidence: 0.40]
def rearrange(word):
    counts = {}
    for ch in word:
        counts[ch] = counts.get(ch, 0) + 1
    if len(counts) == 1:
        return "-1"
    pieces = []
    for ch in sorted(counts):
        pieces.append(ch * counts[ch])
    return "".join(pieces)

# Clause main [Confidence: 1.00]
def main():
    out = []
    for word in read_input():
        out.append(rearrange(word))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

