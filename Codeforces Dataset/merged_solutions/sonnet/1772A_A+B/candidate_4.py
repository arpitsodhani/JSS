import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [bytes(w).decode() for w in data[1:t + 1]]


# --- clause: evaluate :: (text: str) -> int ---
def evaluate(text):
    left = ord(text[0]) - 48
    right = ord(text[2]) - 48
    return left + right


# --- clause: main :: () -> None ---
def main():
    out = []
    for item in read_input():
        out.append(str(evaluate(item)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
