import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[0], raw[1], raw[2], raw[3]


# --- clause: cheapest_path :: (n: int, k: int, a: int, b: int) -> int ---
def cheapest_path(n, k, a, b):
    if k == 1:
        return (n - 1) * a
    running = 0
    x = n
    while x > 1:
        if x < k:
            running += (x - 1) * a
            break
        rest = x % k
        running += rest * a
        x -= rest
        if x == 0:
            break
        drop = (x - x // k) * a
        running += b if b < drop else drop
        x //= k
    return running


# --- clause: main :: () -> None ---
def main():
    n, k, a, b = read_input()
    sys.stdout.write("%d\n" % cheapest_path(n, k, a, b))


if __name__ == "__main__":
    main()
