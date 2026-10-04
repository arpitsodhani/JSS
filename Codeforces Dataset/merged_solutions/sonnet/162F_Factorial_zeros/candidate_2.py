import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n


# --- clause: trailing_zeros :: (n: int) -> int ---
def trailing_zeros(n):
    total = 0
    rest = n
    while rest:
        rest //= 5
        total += rest
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % trailing_zeros(read_input()))


if __name__ == "__main__":
    main()
