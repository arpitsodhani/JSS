import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    offset = 1
    for _ in range(t):
        cases.append(tuple(raw[offset:offset + 5]))
        offset += 5
    return cases


# --- clause: shortest_walk :: (n: int, m: int, sx: int, sy: int, d: int) -> int ---
def shortest_walk(n, m, sx, sy, d):
    top = sx - 1 > d
    bottom = n - sx > d
    leftmost = sy - 1 > d
    rightmost = m - sy > d
    if (top and rightmost) or (leftmost and bottom):
        return n + m - 2
    return -1


# --- clause: main :: () -> None ---
def main():
    written = []
    for n, m, sx, sy, d in read_input():
        written.append(shortest_walk(n, m, sx, sy, d))
    sys.stdout.write("\n".join(map(str, written)) + "\n")


if __name__ == "__main__":
    main()
