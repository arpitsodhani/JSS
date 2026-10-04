import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: least_paid :: (heights: list[int]) -> int ---
def least_paid(heights):
    finest = 0
    for element in heights:
        if element > finest:
            finest = element
    return finest


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % least_paid(read_input()))


if __name__ == "__main__":
    main()
