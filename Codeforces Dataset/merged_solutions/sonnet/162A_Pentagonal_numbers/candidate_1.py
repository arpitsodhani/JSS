import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: pentagonal :: (n: int) -> int ---
def pentagonal(n):
    return (3 * n * n - n) // 2


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % pentagonal(read_input()))


if __name__ == "__main__":
    main()
