import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    text = sys.stdin.buffer.read().decode()
    cut = text.index("\n")
    k = int(text[:cut])
    return k, text[cut + 1:].rstrip("\n")


# --- clause: split_pieces :: (text: str) -> list[int] ---
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


# --- clause: lines_needed :: (pieces: list[int], width: int) -> int ---
def lines_needed(pieces, width):
    lines = 1
    used = 0
    at = 0
    while at < len(pieces):
        piece = pieces[at]
        if piece > width:
            return len(pieces) + 1
        if used + piece > width:
            lines += 1
            used = 0
        used += piece
        at += 1
    return lines


# --- clause: main :: () -> None ---
def main():
    k, text = read_input()
    pieces = split_pieces(text)
    small = max(pieces)
    large = sum(pieces)
    while small < large:
        mid = (small + large) // 2
        if lines_needed(pieces, mid) <= k:
            large = mid
        else:
            small = mid + 1
    sys.stdout.write("%d\n" % small)


if __name__ == "__main__":
    main()
