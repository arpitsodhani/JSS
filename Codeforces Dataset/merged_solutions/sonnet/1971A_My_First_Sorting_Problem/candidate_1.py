import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    return [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(t)]


# --- clause: order_pair :: (x: int, y: int) -> tuple[int, int] ---
def order_pair(x, y):
    if x <= y:
        return x, y
    return y, x


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, y in read_input():
        out.append("%d %d" % order_pair(x, y))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
