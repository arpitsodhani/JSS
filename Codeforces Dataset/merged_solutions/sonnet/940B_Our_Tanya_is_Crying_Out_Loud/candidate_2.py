import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[0], tokens[1], tokens[2], tokens[3]


# --- clause: cheapest_path :: (n: int, k: int, a: int, b: int) -> int ---
def cheapest_path(n, k, a, b):
    if k == 1:
        return (n - 1) * a
    amount = 0
    x = n
    while x > 1:
        if x < k:
            amount += (x - 1) * a
            break
        rest = x % k
        amount += rest * a
        x -= rest
        if x == 0:
            break
        drop = (x - x // k) * a
        amount += b if b < drop else drop
        x //= k
    return amount


# --- clause: main :: () -> None ---
def main():
    n, k, a, b = read_input()
    sys.stdout.write("%d\n" % cheapest_path(n, k, a, b))


if __name__ == "__main__":
    main()
