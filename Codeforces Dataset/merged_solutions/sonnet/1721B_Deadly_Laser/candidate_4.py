import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    reader = 1
    for _ in range(t):
        cases.append(tuple(numbers[reader:reader + 5]))
        reader += 5
    return cases


# --- clause: shortest_walk :: (n: int, m: int, sx: int, sy: int, d: int) -> int ---
def shortest_walk(n, m, sx, sy, d):
    over_top = True
    for y in range(1, m + 1):
        if sx - 1 + abs(y - sy) <= d:
            over_top = False
            break
    down_right = True
    for x in range(1, n + 1):
        if abs(x - sx) + m - sy <= d:
            down_right = False
            break
    down_left = True
    for x in range(1, n + 1):
        if abs(x - sx) + sy - 1 <= d:
            down_left = False
            break
    along_bottom = True
    for y in range(1, m + 1):
        if n - sx + abs(y - sy) <= d:
            along_bottom = False
            break
    if (over_top and down_right) or (down_left and along_bottom):
        return n + m - 2
    return -1


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m, sx, sy, d in read_input():
        out.append(shortest_walk(n, m, sx, sy, d))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
