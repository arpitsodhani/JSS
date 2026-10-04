import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    words = []
    for i in range(t):
        words.append(raw[2 + 2 * i].decode())
    return words


# --- clause: smallest_missing :: (word: str) -> str ---
def smallest_missing(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    n = len(word)
    for span in (1, 2, 3):
        present = set()
        for i in range(n - span + 1):
            present.add(word[i:i + span])
        stack = [""]
        while stack:
            piece = stack.pop()
            if len(piece) == span:
                if piece not in present:
                    return piece
                continue
            for ch in reversed(letters):
                stack.append(piece + ch)
    return ""


# --- clause: main :: () -> None ---
def main():
    lines = []
    for word in read_input():
        lines.append(smallest_missing(word))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
