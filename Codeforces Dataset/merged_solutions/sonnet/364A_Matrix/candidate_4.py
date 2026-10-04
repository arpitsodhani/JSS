import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    if len(data) == 1:
        return int(data[0]), ""
    return int(data[0]), bytes(data[1]).decode()


# --- clause: interval_counts :: (digits: str) -> list[int] ---
def interval_counts(digits):
    n = len(digits)
    counts = [0] * (9 * n + 2)
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
        whole = 0
        for value in counts:
            whole += value
        zero = counts[0]
        return 2 * zero * whole - zero * zero
    total = 0
    for left in range(1, top + 1):
        if counts[left] == 0 or a % left:
            continue
        right = a // left
        if right <= top:
            total += counts[left] * counts[right]
    return total


# --- clause: main :: () -> None ---
def main():
    a, digits = read_input()
    counts = interval_counts(digits)
    sys.stdout.write(str(count_rectangles(a, counts)) + "\n")


if __name__ == "__main__":
    main()
