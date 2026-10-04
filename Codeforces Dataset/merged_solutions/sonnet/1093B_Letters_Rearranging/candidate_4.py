import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[i + 1].decode() for i in range(t)]


# --- clause: rearrange :: (word: str) -> str ---
def rearrange(word):
    smallest = min(word)
    largest = max(word)
    if smallest == largest:
        return "-1"
    head = smallest * word.count(smallest)
    tail = []
    for ch in sorted(word):
        if ch != smallest:
            tail.append(ch)
    return head + "".join(tail)


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(rearrange(word))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
