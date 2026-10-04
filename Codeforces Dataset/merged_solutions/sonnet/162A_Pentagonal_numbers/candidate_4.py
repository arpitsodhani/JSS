import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: pentagonal :: (n: int) -> int ---
def pentagonal(n):
    total = 0
    for i in range(n):
        total += 1 + 3 * i
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % pentagonal(read_input()))


if __name__ == "__main__":
    main()
