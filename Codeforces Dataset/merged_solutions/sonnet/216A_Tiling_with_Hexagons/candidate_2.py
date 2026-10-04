import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[0], tokens[1], tokens[2]


# --- clause: count_tiles :: (a: int, b: int, c: int) -> int ---
def count_tiles(a, b, c):
    return a * b + b * c + c * a - a - b - c + 1


# --- clause: main :: () -> None ---
def main():
    a, b, c = read_input()
    sys.stdout.write("%d\n" % count_tiles(a, b, c))


if __name__ == "__main__":
    main()
