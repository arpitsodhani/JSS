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
    for piece in pieces:
        if piece > width:
            return len(pieces) + 1
        if used + piece <= width:
            used += piece
        else:
            lines += 1
            used = piece
    return lines


# --- clause: main :: () -> None ---
def main():
    k, text = read_input()
    pieces = split_pieces(text)
    floor_value = max(pieces)
    ceiling_value = sum(pieces)
    while floor_value < ceiling_value:
        mid = (floor_value + ceiling_value) // 2
        if lines_needed(pieces, mid) <= k:
            ceiling_value = mid
        else:
            floor_value = mid + 1
    sys.stdout.write("%d\n" % floor_value)


if __name__ == "__main__":
    main()
