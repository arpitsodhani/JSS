import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: best_distance :: (n: int, a: list[int]) -> int ---
def best_distance(n, a):
    low = a.index(min(a))
    high = a.index(max(a))
    far_low = low if low > n - 1 - low else n - 1 - low
    far_high = high if high > n - 1 - high else n - 1 - high
    return far_low if far_low > far_high else far_high


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    sys.stdout.write(str(best_distance(n, a)) + "\n")


if __name__ == "__main__":
    main()
