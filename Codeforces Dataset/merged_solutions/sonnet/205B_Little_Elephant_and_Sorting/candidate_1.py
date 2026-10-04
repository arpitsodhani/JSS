import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: lifting_moves :: (a: list[int]) -> int ---
def lifting_moves(a):
    total = 0
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            total += a[i - 1] - a[i]
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % lifting_moves(read_input()))


if __name__ == "__main__":
    main()
