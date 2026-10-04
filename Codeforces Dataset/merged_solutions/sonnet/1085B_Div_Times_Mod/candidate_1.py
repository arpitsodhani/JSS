import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1])


# --- clause: smallest_x :: (n: int, k: int) -> int ---
def smallest_x(n, k):
    best = None
    for r in range(1, k):
        if n % r:
            continue
        value = (n // r) * k + r
        if best is None or value < best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write("%d\n" % smallest_x(n, k))


if __name__ == "__main__":
    main()
