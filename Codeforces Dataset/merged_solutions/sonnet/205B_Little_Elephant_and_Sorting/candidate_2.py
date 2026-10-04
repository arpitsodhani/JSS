import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: lifting_moves :: (a: list[int]) -> int ---
def lifting_moves(a):
    total = 0
    peak = a[0] if a else 0
    for value in a:
        if value < peak:
            total += peak - value
            peak = value
        else:
            peak = value
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % lifting_moves(read_input()))


if __name__ == "__main__":
    main()
