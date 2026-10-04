import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    words = []
    for i in range(t):
        words.append(fields[2 + 2 * i].decode())
    return words


# --- clause: smallest_missing :: (word: str) -> str ---
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


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for word in read_input():
        pieces.append(smallest_missing(word))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
