import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [bytes(w).decode() for w in data[1:n + 1]]


# --- clause: shorten :: (word: str) -> str ---
def shorten(word):
    if len(word) <= 10:
        return word
    inner = str(len(word) - 2)
    return word[0] + inner + word[len(word) - 1]


# --- clause: main :: () -> None ---
def main():
    out = []
    for item in read_input():
        out.append(shorten(item))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
