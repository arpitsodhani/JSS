import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    return raw[1:1 + n], raw[1 + n:1 + 2 * n]


# --- clause: count_good :: (a: list[int], b: list[int]) -> int ---
def count_good(a, b):
    gaps = sorted(a[i] - b[i] for i in range(len(a)))
    total = 0
    low = 0
    second_side = len(gaps) - 1
    while low < second_side:
        if gaps[low] + gaps[second_side] > 0:
            total += second_side - low
            second_side -= 1
        else:
            low += 1
    return total


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % count_good(a, b))


if __name__ == "__main__":
    main()
