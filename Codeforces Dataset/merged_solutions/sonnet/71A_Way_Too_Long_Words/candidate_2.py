import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [str(word, "ascii") for word in data[1:1 + n]]


# --- clause: shorten :: (word: str) -> str ---
def shorten(word):
    size = len(word)
    if size > 10:
        return "%s%d%s" % (word[0], size - 2, word[size - 1])
    return word


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(shorten(word))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
