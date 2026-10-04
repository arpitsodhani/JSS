import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2], numbers[3]


# --- clause: cheapest_path :: (n: int, k: int, a: int, b: int) -> int ---
def cheapest_path(n, k, a, b):
    if k == 1:
        return (n - 1) * a
    steps = []
    x = n
    while x >= k:
        steps.append(x)
        x //= k
    total = (x - 1) * a
    for value in steps:
        landing = value // k
        total += (value - landing * k) * a
        jump = (landing * k - landing) * a
        total += b if b < jump else jump
    return total


# --- clause: main :: () -> None ---
def main():
    n, k, a, b = read_input()
    sys.stdout.write("%d\n" % cheapest_path(n, k, a, b))


if __name__ == "__main__":
    main()
