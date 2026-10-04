import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return data[1:1 + n], data[1 + n:1 + 2 * n]


# --- clause: count_good :: (a: list[int], b: list[int]) -> int ---
def count_good(a, b):
    gaps = sorted(a[i] - b[i] for i in range(len(a)))
    total = 0
    left = 0
    right = len(gaps) - 1
    while left < right:
        if gaps[left] + gaps[right] > 0:
            total += right - left
            right -= 1
        else:
            left += 1
    return total


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % count_good(a, b))


if __name__ == "__main__":
    main()
