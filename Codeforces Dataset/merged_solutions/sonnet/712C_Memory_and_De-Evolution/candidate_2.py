import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1])


# --- clause: grow_steps :: (x: int, y: int) -> int ---
def grow_steps(x, y):
    a = y
    b = y
    c = y
    steps = 0
    while a < x or b < x or c < x:
        if a <= b and a <= c:
            a = min(x, b + c - 1)
        elif b <= a and b <= c:
            b = min(x, a + c - 1)
        else:
            c = min(x, a + b - 1)
        steps += 1
    return steps


# --- clause: main :: () -> None ---
def main():
    x, y = read_input()
    sys.stdout.write("%d\n" % grow_steps(x, y))


if __name__ == "__main__":
    main()
