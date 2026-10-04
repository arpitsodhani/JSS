import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    text = sys.stdin.buffer.read().decode()
    cut = text.index("\n")
    k = int(text[:cut])
    return k, text[cut + 1:].rstrip("\n")

# Clause split_pieces [Confidence: 1.00]
def split_pieces(text):
    pieces = []
    width = 0
    for ch in text:
        width += 1
        if ch == "-" or ch == " ":
            pieces.append(width)
            width = 0
    if width:
        pieces.append(width)
    return pieces

# Clause lines_needed [Confidence: 1.00]
def lines_needed(pieces, width):
    lines = 1
    used = 0
    for piece in pieces:
        if piece > width:
            return len(pieces) + 1
        if used + piece <= width:
            used += piece
        else:
            lines += 1
            used = piece
    return lines

# Clause main [Confidence: 1.00]
def main():
    k, text = read_input()
    pieces = split_pieces(text)
    bottom = max(pieces)
    top_value = sum(pieces)
    while bottom < top_value:
        mid = (bottom + top_value) // 2
        if lines_needed(pieces, mid) <= k:
            top_value = mid
        else:
            bottom = mid + 1
    sys.stdout.write("%d\n" % bottom)


if __name__ == "__main__":
    main()

