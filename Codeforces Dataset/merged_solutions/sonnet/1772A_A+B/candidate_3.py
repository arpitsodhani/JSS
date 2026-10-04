import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    rows = []
    for i in range(t):
        rows.append(data[1 + i].decode())
    return rows


# --- clause: evaluate :: (text: str) -> int ---
def evaluate(text):
    total = 0
    for ch in text:
        if ch != "+":
            total += ord(ch) - 48
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for text in read_input():
        out.append(str(evaluate(text)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
