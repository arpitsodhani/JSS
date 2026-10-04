import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


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
    lines = []
    for n in read_input():
        lines.append("%d %d" % split_pair(n))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
