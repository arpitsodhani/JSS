import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: total_segments :: (a: int, b: int) -> int ---
def total_segments(a, b):
    per_digit = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
    total = 0
    for number in range(a, b + 1):
        value = number
        while value:
            total += per_digit[value % 10]
            value //= 10
    return total


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write(str(total_segments(a, b)) + "\n")


if __name__ == "__main__":
    main()
