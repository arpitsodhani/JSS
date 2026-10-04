import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])


# --- clause: trailing_zeros :: (n: int) -> int ---
def trailing_zeros(n):
    total = 0
    for exponent in range(1, 30):
        power = 5 ** exponent
        if power > n:
            break
        total += n // power
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(trailing_zeros(read_input())) + "\n")


if __name__ == "__main__":
    main()
