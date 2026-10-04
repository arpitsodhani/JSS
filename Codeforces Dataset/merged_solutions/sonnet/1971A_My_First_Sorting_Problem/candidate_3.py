import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    return [(fields[1 + 2 * i], fields[2 + 2 * i]) for i in range(t)]


# --- clause: order_pair :: (x: int, y: int) -> tuple[int, int] ---
def order_pair(x, y):
    if x <= y:
        return x, y
    return y, x


# --- clause: main :: () -> None ---
def main():
    collected = []
    for x, y in read_input():
        collected.append("%d %d" % order_pair(x, y))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
