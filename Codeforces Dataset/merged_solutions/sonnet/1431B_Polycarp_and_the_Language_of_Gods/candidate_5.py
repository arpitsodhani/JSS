import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    return [raw[1 + i].decode() for i in range(t)]


# --- clause: count_marks :: (s: str) -> int ---
def count_marks(s):
    running = 0
    run = 0
    for ch in s:
        if ch == "v":
            run += 1
        else:
            running += run // 2 + 1
            run = 0
    running += run // 2
    return running


# --- clause: main :: () -> None ---
def main():
    lines = []
    for s in read_input():
        lines.append(count_marks(s))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
