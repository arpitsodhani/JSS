import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0].decode())


# --- clause: press_counts :: (n: int) -> list[str] ---
def press_counts(n):
    out = ["2"]
    for level in range(2, n + 1):
        out.append(str(level * (level + 1) * (level + 1) - (level - 1)))
    del out[n:]
    return out


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("\n".join(press_counts(n)) + "\n")


if __name__ == "__main__":
    main()
