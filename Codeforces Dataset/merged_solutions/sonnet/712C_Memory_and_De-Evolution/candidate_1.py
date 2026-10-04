import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    x = int(data[0])
    y = int(data[1])
    return x, y


# --- clause: grow_steps :: (x: int, y: int) -> int ---
def grow_steps(x, y):
    sides = [y, y, y]
    steps = 0
    while sides[0] < x:
        limit = sides[1] + sides[2] - 1
        if limit > x:
            limit = x
        sides[0] = limit
        sides.sort()
        steps += 1
    return steps


# --- clause: main :: () -> None ---
def main():
    x, y = read_input()
    sys.stdout.write(str(grow_steps(x, y)) + "\n")


if __name__ == "__main__":
    main()
