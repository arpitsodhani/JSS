import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    return numbers[1:1 + n], numbers[1 + n:1 + 2 * n]


# --- clause: count_good :: (a: list[int], b: list[int]) -> int ---
def count_good(a, b):
    gaps = sorted(a[i] - b[i] for i in range(len(a)))
    n = len(gaps)
    total = 0
    for i in range(n):
        want = -gaps[i]
        low = i + 1
        high = n
        while low < high:
            mid = (low + high) // 2
            if gaps[mid] > want:
                high = mid
            else:
                low = mid + 1
        total += n - low
    return total


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % count_good(a, b))


if __name__ == "__main__":
    main()
