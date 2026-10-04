import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return int(raw[0]), int(raw[1])


# --- clause: settle :: (a: int, b: int) -> tuple[int, int] ---
def settle(a, b):
    while a and b:
        if a >= 2 * b:
            a %= 2 * b
        elif b >= 2 * a:
            b %= 2 * a
        else:
            break
    return a, b


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write("%d %d\n" % settle(a, b))


if __name__ == "__main__":
    main()
