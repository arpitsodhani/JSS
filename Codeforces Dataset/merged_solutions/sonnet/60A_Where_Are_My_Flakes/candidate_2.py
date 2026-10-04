import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[str, int]]] ---
def read_input():
    lines = sys.stdin.buffer.read().decode().split("\n")
    n, m = (int(v) for v in lines[0].split())
    hints = []
    for i in range(1, m + 1):
        parts = lines[i].split()
        hints.append((parts[2], int(parts[-1])))
    return n, hints


# --- clause: count_boxes :: (n: int, hints: list[tuple[str, int]]) -> int ---
def count_boxes(n, hints):
    bottom = 1
    high = n
    for side, spot in hints:
        if side == "left":
            if spot - 1 < high:
                high = spot - 1
        else:
            if spot + 1 > bottom:
                bottom = spot + 1
    if bottom > high:
        return -1
    return high - bottom + 1


# --- clause: main :: () -> None ---
def main():
    n, hints = read_input()
    sys.stdout.write("%d\n" % count_boxes(n, hints))


if __name__ == "__main__":
    main()
