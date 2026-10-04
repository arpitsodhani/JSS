import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: destroy_steps :: (h: list[int]) -> int ---
def destroy_steps(h):
    n = len(h)
    left = [0] * n
    left[0] = 1 if h[0] else 0
    for i in range(1, n):
        step = left[i - 1] + 1
        left[i] = step if step < h[i] else h[i]
    top = 0
    second_side = 0
    for i in range(n - 1, -1, -1):
        step = second_side + 1
        second_side = step if step < h[i] else h[i]
        here = second_side if second_side < left[i] else left[i]
        if here > top:
            top = here
    return top


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % destroy_steps(read_input()))


if __name__ == "__main__":
    main()
