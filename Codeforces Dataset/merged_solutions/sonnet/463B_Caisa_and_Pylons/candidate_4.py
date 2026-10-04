import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: least_paid :: (heights: list[int]) -> int ---
def least_paid(heights):
    return max(heights)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % least_paid(read_input()))


if __name__ == "__main__":
    main()
