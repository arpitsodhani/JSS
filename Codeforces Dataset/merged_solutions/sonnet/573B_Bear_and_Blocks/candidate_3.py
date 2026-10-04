import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: destroy_steps :: (h: list[int]) -> int ---
def destroy_steps(h):
    n = len(h)
    left = [0] * n
    left[0] = 1 if h[0] else 0
    for i in range(1, n):
        step = left[i - 1] + 1
        left[i] = step if step < h[i] else h[i]
    finest = 0
    finish = 0
    for i in range(n - 1, -1, -1):
        step = finish + 1
        finish = step if step < h[i] else h[i]
        here = finish if finish < left[i] else left[i]
        if here > finest:
            finest = here
    return finest


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % destroy_steps(read_input()))


if __name__ == "__main__":
    main()
