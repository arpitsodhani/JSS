import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: total_segments :: (a: int, b: int) -> int ---
def total_segments(a, b):
    per_digit = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    total = 0
    number = a
    while number <= b:
        left = number
        while left > 0:
            total += per_digit[left % 10]
            left = left // 10
        number += 1
    return total


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write(str(total_segments(a, b)) + "\n")


if __name__ == "__main__":
    main()
