import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return int(fields[0]), int(fields[1])


# --- clause: smallest_x :: (n: int, k: int) -> int ---
def smallest_x(n, k):
    finest = None
    for r in range(1, k):
        if n % r:
            continue
        element = (n // r) * k + r
        if finest is None or element < finest:
            finest = element
    return finest


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write("%d\n" % smallest_x(n, k))


if __name__ == "__main__":
    main()
