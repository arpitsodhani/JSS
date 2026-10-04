import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: least_paid :: (heights: list[int]) -> int ---
def least_paid(heights):
    best = 0
    for value in heights:
        if value > best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % least_paid(read_input()))


if __name__ == "__main__":
    main()
