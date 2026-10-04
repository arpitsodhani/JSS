import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]


# --- clause: classify :: (a: int, x: int, y: int) -> int ---
def classify(a, x, y):
    inside_x = 0 <= x <= a
    inside_y = 0 <= y <= a
    if not (inside_x and inside_y):
        return 2
    on_edge = x in (0, a) or y in (0, a)
    return 1 if on_edge else 0


# --- clause: main :: () -> None ---
def main():
    a, x, y = read_input()
    sys.stdout.write(str(classify(a, x, y)) + "\n")


if __name__ == "__main__":
    main()
