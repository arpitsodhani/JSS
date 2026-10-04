import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: least_paid :: (heights: list[int]) -> int ---
def least_paid(heights):
    best = 0
    for item in heights:
        if item > best:
            best = item
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % least_paid(read_input()))


if __name__ == "__main__":
    main()
