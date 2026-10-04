import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]


# --- clause: count_decks :: (b: int, g: int, n: int) -> int ---
def count_decks(b, g, n):
    return min(n, b) - max(0, n - g) + 1


# --- clause: main :: () -> None ---
def main():
    b, g, n = read_input()
    sys.stdout.write(str(count_decks(b, g, n)) + "\n")


if __name__ == "__main__":
    main()
