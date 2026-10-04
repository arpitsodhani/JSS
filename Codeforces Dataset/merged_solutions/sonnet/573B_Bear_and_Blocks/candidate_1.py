import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: destroy_steps :: (h: list[int]) -> int ---
def destroy_steps(h):
    n = len(h)
    left = [0] * n
    left[0] = 1 if h[0] else 0
    for i in range(1, n):
        step = left[i - 1] + 1
        left[i] = step if step < h[i] else h[i]
    best = 0
    right = 0
    for i in range(n - 1, -1, -1):
        step = right + 1
        right = step if step < h[i] else h[i]
        here = right if right < left[i] else left[i]
        if here > best:
            best = here
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % destroy_steps(read_input()))


if __name__ == "__main__":
    main()
