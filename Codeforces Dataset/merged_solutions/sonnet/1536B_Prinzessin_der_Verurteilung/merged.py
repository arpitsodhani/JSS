import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    words = []
    for i in range(t):
        words.append(data[2 + 2 * i].decode())
    return words

# Clause smallest_missing [Confidence: 1.00]
def smallest_missing(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    n = len(word)
    for extent in (1, 2, 3):
        present = set()
        for i in range(n - extent + 1):
            present.add(word[i:i + extent])
        stack = [""]
        while stack:
            piece = stack.pop()
            if len(piece) == extent:
                if piece not in present:
                    return piece
                continue
            for ch in reversed(letters):
                stack.append(piece + ch)
    return ""

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for word in read_input():
        lines.append(smallest_missing(word))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

