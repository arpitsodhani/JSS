import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n


# --- clause: press_counts :: (n: int) -> list[str] ---
def press_counts(n):
    out = ["2"]
    level = 2
    while level <= n:
        out.append(str(level * (level + 1) ** 2 - level + 1))
        level += 1
    return out[:n]


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%s\n" % "\n".join(press_counts(read_input())))


if __name__ == "__main__":
    main()
