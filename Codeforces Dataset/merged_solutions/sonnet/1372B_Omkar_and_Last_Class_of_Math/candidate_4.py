import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: split_pair :: (n: int) -> tuple[int, int] ---
def split_pair(n):
    biggest = 1
    d = 1
    while d * d <= n:
        if n % d == 0:
            other = n // d
            if other < n and other > biggest:
                biggest = other
            if d < n and d > biggest:
                biggest = d
        d += 1
    return biggest, n - biggest


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n in read_input():
        pieces.append("%d %d" % split_pair(n))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
