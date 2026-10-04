import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    return int(tokens[0]), int(tokens[1])


# --- clause: smallest_x :: (n: int, k: int) -> int ---
def smallest_x(n, k):
    best = None
    for r in range(1, k):
        if n % r:
            continue
        item = (n // r) * k + r
        if best is None or item < best:
            best = item
    return best


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write("%d\n" % smallest_x(n, k))


if __name__ == "__main__":
    main()
