import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]


# --- clause: evaluate :: (text: str) -> int ---
def evaluate(text):
    left = int(text[0])
    right = int(text[2])
    return left + right


# --- clause: main :: () -> None ---
def main():
    out = []
    for text in read_input():
        out.append(str(evaluate(text)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
