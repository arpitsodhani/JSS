import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: fewest_bacteria :: (x: int) -> int ---
def fewest_bacteria(x):
    total = 0
    while x:
        total += x % 2
        x //= 2
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_bacteria(read_input()))


if __name__ == "__main__":
    main()
