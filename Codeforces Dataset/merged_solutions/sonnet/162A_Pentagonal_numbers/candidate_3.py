import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: pentagonal :: (n: int) -> int ---
def pentagonal(n):
    half = (3 * n - 1)
    return (n * half) >> 1


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % pentagonal(read_input()))


if __name__ == "__main__":
    main()
