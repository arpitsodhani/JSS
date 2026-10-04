import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    return [(raw[1 + 2 * i], raw[2 + 2 * i]) for i in range(t)]


# --- clause: order_pair :: (x: int, y: int) -> tuple[int, int] ---
def order_pair(x, y):
    if x <= y:
        return x, y
    return y, x


# --- clause: main :: () -> None ---
def main():
    written = []
    for x, y in read_input():
        written.append("%d %d" % order_pair(x, y))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
