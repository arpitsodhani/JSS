import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: least_paid :: (heights: list[int]) -> int ---
def least_paid(heights):
    top = 0
    for number in heights:
        if number > top:
            top = number
    return top


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % least_paid(read_input()))


if __name__ == "__main__":
    main()
