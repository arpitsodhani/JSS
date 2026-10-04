import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return int(numbers[0]), int(numbers[1])


# --- clause: smallest_x :: (n: int, k: int) -> int ---
def smallest_x(n, k):
    best = None
    d = 1
    while d * d <= n:
        if n % d == 0:
            for r in (d, n // d):
                if r < k:
                    value = (n // r) * k + r
                    if best is None or value < best:
                        best = value
        d += 1
    return best


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write("%d\n" % smallest_x(n, k))


if __name__ == "__main__":
    main()
