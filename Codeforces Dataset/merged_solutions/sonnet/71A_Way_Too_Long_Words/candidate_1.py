import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[1 + i].decode() for i in range(n)]


# --- clause: shorten :: (word: str) -> str ---
def shorten(word):
    if len(word) <= 10:
        return word
    return word[0] + str(len(word) - 2) + word[-1]


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(shorten(word))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
