import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]


# --- clause: classify :: (a: int, x: int, y: int) -> int ---
def classify(a, x, y):
    if 0 < x and x < a and 0 < y and y < a:
        return 0
    if x >= 0 and x <= a and y >= 0 and y <= a:
        return 1
    return 2


# --- clause: main :: () -> None ---
def main():
    a, x, y = read_input()
    sys.stdout.write(str(classify(a, x, y)) + "\n")


if __name__ == "__main__":
    main()
