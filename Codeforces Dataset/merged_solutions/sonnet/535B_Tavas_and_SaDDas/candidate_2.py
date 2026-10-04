import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: lucky_index :: (n: str) -> int ---
def lucky_index(n):
    width = len(n)
    shorter = (1 << width) - 2
    inside = 0
    for ch in n:
        inside = inside * 2 + (1 if ch == "7" else 0)
    return shorter + inside + 1


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % lucky_index(read_input()))


if __name__ == "__main__":
    main()
