import sys


# --- clause: read_input :: () -> tuple[list[int], int, list[int], int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    bx = data[1]
    x = data[2:2 + n]
    pos = 2 + n
    m = data[pos]
    by = data[pos + 1]
    y = data[pos + 2:pos + 2 + m]
    return x, bx, y, by


# --- clause: to_number :: (digits: list[int], base: int) -> int ---
def to_number(digits, base):
    value = 0
    for digit in digits:
        value = value * base
        value += digit
    return value


# --- clause: main :: () -> None ---
def main():
    x, bx, y, by = read_input()
    left = to_number(x, bx)
    right = to_number(y, by)
    if left < right:
        sys.stdout.write("<\n")
    elif left > right:
        sys.stdout.write(">\n")
    else:
        sys.stdout.write("=\n")


if __name__ == "__main__":
    main()
