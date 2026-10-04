import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    cursor = 1
    for _ in range(t):
        cases.append(tuple(fields[cursor:cursor + 5]))
        cursor += 5
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
    collected = []
    for n, m, sx, sy, d in read_input():
        collected.append(shortest_walk(n, m, sx, sy, d))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()
