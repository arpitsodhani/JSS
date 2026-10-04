import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    return [tokens[1 + i].decode() for i in range(t)]


# --- clause: count_marks :: (s: str) -> int ---
def count_marks(s):
    amount = 0
    run = 0
    for ch in s:
        if ch == "v":
            run += 1
        else:
            amount += run // 2 + 1
            run = 0
    amount += run // 2
    return amount


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(count_marks(s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
