import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[1 + i].decode() for i in range(n)]

# Clause shorten [Confidence: 0.60]
def shorten(word):
    if len(word) <= 10:
        return word
    return word[0] + str(len(word) - 2) + word[-1]

# Clause main [Confidence: 1.00]
def main():
    out = []
    for item in read_input():
        out.append(shorten(item))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

