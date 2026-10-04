import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    x = numbers[1]
    return x, numbers[2:2 + n]


# --- clause: best_beauty :: (x: int, a: list[int]) -> int ---
def best_beauty(x, a):
    n = len(a)
    left = [0] * (n + 1)
    for i in range(n):
        step = left[i] + a[i]
        left[i + 1] = step if step > 0 else 0
    right = [0] * (n + 2)
    for i in range(n - 1, -1, -1):
        step = right[i + 1] + a[i]
        right[i] = step if step > 0 else 0
    best = 0
    for value in left:
        if value > best:
            best = value
    running = -(1 << 62)
    for i in range(n):
        base = running if running > left[i] else left[i]
        running = base + a[i] * x
        here = running + right[i + 1]
        if here > best:
            best = here
    return best


# --- clause: main :: () -> None ---
def main():
    x, a = read_input()
    sys.stdout.write("%d\n" % best_beauty(x, a))


if __name__ == "__main__":
    main()
