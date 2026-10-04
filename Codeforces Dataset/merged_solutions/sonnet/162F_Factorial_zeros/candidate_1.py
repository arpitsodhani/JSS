import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])


# --- clause: trailing_zeros :: (n: int) -> int ---
def trailing_zeros(n):
    total = 0
    power = 5
    while power <= n:
        total += n // power
        power *= 5
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(trailing_zeros(read_input())) + "\n")


if __name__ == "__main__":
    main()
