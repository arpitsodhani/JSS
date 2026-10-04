import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[i].decode() for i in range(1, n + 1)]


# --- clause: shorten :: (word: str) -> str ---
def shorten(word):
    size = len(word)
    return word if size <= 10 else word[0] + str(size - 2) + word[-1]


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(shorten(word))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
