import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    return [fields[1 + i].decode() for i in range(t)]


# --- clause: count_marks :: (s: str) -> int ---
def count_marks(s):
    tally = 0
    run = 0
    for ch in s:
        if ch == "v":
            run += 1
        else:
            tally += run // 2 + 1
            run = 0
    tally += run // 2
    return tally


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for s in read_input():
        pieces.append(count_marks(s))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
