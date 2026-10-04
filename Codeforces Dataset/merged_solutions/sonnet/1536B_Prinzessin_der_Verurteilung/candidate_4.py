import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    words = []
    for i in range(t):
        words.append(numbers[2 + 2 * i].decode())
    return words


# --- clause: smallest_missing :: (word: str) -> str ---
def smallest_missing(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    n = len(word)
    for length_of in (1, 2, 3):
        present = set()
        for i in range(n - length_of + 1):
            present.add(word[i:i + length_of])
        stack = [""]
        while stack:
            piece = stack.pop()
            if len(piece) == length_of:
                if piece not in present:
                    return piece
                continue
            for ch in reversed(letters):
                stack.append(piece + ch)
    return ""


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(smallest_missing(word))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
