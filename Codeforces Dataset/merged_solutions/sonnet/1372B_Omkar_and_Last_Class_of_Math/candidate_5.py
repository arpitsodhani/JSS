import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: split_pair :: (n: int) -> tuple[int, int] ---
def split_pair(n):
    factor = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            factor = d
            break
        d += 1
    if factor == 1:
        return 1, n - 1
    part = n // factor
    return part, n - part


# --- clause: main :: () -> None ---
def main():
    written = []
    for n in read_input():
        written.append("%d %d" % split_pair(n))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
