import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    if len(data) < 2:
        return int(data[0]), ""
    return int(data[0]), data[1].decode()


# --- clause: interval_counts :: (digits: str) -> list[int] ---
def interval_counts(digits):
    n = len(digits)
    counts = [0] * (9 * n + 1)
    for start in range(n):
        total = 0
        for end in range(start, n):
            total += ord(digits[end]) - 48
            counts[total] += 1
    return counts


# --- clause: count_rectangles :: (a: int, counts: list[int]) -> int ---
def count_rectangles(a, counts):
    top = len(counts) - 1
    if a == 0:
        whole = sum(counts)
        zero = counts[0]
        return zero * (whole - zero) * 2 + zero * zero
    total = 0
    left = 1
    while left <= top:
        if counts[left] and a % left == 0:
            right = a // left
            if right <= top:
                total += counts[left] * counts[right]
        left += 1
    return total


# --- clause: main :: () -> None ---
def main():
    a, digits = read_input()
    print(count_rectangles(a, interval_counts(digits)))


if __name__ == "__main__":
    main()
