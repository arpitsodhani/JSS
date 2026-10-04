import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: lifting_moves :: (a: list[int]) -> int ---
def lifting_moves(a):
    running = 0
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            running += a[i - 1] - a[i]
    return running


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % lifting_moves(read_input()))


if __name__ == "__main__":
    main()
