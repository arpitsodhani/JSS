import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    x = int(data[0])
    y = int(data[1])
    return x, y


# --- clause: grow_steps :: (x: int, y: int) -> int ---
def grow_steps(x, y):
    low = y
    mid = y
    top = y
    steps = 0
    while low < x:
        grown = mid + top - 1
        if grown > x:
            grown = x
        if grown < top:
            low, mid, top = mid, grown, top
        else:
            low, mid, top = mid, top, grown
        steps += 1
    return steps


# --- clause: main :: () -> None ---
def main():
    x, y = read_input()
    print(grow_steps(x, y))


if __name__ == "__main__":
    main()
