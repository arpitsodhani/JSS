import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: fewest_bacteria :: (x: int) -> int ---
def fewest_bacteria(x):
    return bin(x).count("1")


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_bacteria(read_input()))


if __name__ == "__main__":
    main()
