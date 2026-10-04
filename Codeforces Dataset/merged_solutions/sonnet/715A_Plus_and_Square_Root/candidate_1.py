import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])


# --- clause: press_counts :: (n: int) -> list[str] ---
def press_counts(n):
    out = ["2"]
    for level in range(2, n + 1):
        out.append(str(level * (level + 1) * (level + 1) - (level - 1)))
    return out[:n]


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(press_counts(read_input())) + "\n")


if __name__ == "__main__":
    main()
