import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: lifting_moves :: (a: list[int]) -> int ---
def lifting_moves(a):
    summed = 0
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            summed += a[i - 1] - a[i]
    return summed


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % lifting_moves(read_input()))


if __name__ == "__main__":
    main()
