import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    x = int(data[0])
    y = int(data[-1])
    return x, y


# --- clause: grow_steps :: (x: int, y: int) -> int ---
def grow_steps(x, y):
    heap = [y, y, y]
    steps = 0
    while heap[0] < x:
        heap[0] = min(x, heap[1] + heap[2] - 1)
        heap = sorted(heap)
        steps += 1
    return steps


# --- clause: main :: () -> None ---
def main():
    x, y = read_input()
    sys.stdout.write(str(grow_steps(x, y)) + "\n")


if __name__ == "__main__":
    main()
