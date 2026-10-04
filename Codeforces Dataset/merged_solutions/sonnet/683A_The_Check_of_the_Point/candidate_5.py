import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]


# --- clause: classify :: (a: int, x: int, y: int) -> int ---
def classify(a, x, y):
    outside = x < 0 or x > a or y < 0 or y > a
    if outside:
        return 2
    border = x == 0 or x == a or y == 0 or y == a
    if border:
        return 1
    return 0


# --- clause: main :: () -> None ---
def main():
    a, x, y = read_input()
    sys.stdout.write(str(classify(a, x, y)) + "\n")


if __name__ == "__main__":
    main()
