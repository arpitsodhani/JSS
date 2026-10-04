import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[-1])


# --- clause: trailing_zeros :: (n: int) -> int ---
def trailing_zeros(n):
    power = 5
    total = 0
    while power <= n:
        total += n // power
        power *= 5
    return total


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write(str(trailing_zeros(n)) + "\n")


if __name__ == "__main__":
    main()
