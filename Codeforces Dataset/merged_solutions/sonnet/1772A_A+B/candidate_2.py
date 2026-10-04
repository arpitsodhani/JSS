import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [str(w, "ascii") for w in data[1:1 + t]]


# --- clause: evaluate :: (text: str) -> int ---
def evaluate(text):
    parts = text.split("+")
    return int(parts[0]) + int(parts[1])


# --- clause: main :: () -> None ---
def main():
    out = []
    for text in read_input():
        out.append(str(evaluate(text)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
