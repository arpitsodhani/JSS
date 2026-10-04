import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return int(raw[0]), int(raw[1])


# --- clause: smallest_x :: (n: int, k: int) -> int ---
def smallest_x(n, k):
    top = None
    for r in range(1, k):
        if n % r:
            continue
        number = (n // r) * k + r
        if top is None or number < top:
            top = number
    return top


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write("%d\n" % smallest_x(n, k))


if __name__ == "__main__":
    main()
