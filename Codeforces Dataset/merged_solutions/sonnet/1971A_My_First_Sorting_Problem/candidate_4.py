import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    return [(numbers[1 + 2 * i], numbers[2 + 2 * i]) for i in range(t)]


# --- clause: order_pair :: (x: int, y: int) -> tuple[int, int] ---
def order_pair(x, y):
    both = [x, y]
    both.sort()
    return both[0], both[1]


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for x, y in read_input():
        pieces.append("%d %d" % order_pair(x, y))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
