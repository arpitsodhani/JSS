import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]


# --- clause: rearrange :: (word: str) -> str ---
def rearrange(word):
    letters = sorted(word)
    if letters[0] == letters[-1]:
        return "-1"
    return "".join(letters)


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(rearrange(word))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
