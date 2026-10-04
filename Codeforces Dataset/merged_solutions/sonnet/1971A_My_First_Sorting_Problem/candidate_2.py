import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    return [(tokens[1 + 2 * i], tokens[2 + 2 * i]) for i in range(t)]


# --- clause: order_pair :: (x: int, y: int) -> tuple[int, int] ---
def order_pair(x, y):
    if x <= y:
        return x, y
    return y, x


# --- clause: main :: () -> None ---
def main():
    lines = []
    for x, y in read_input():
        lines.append("%d %d" % order_pair(x, y))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
