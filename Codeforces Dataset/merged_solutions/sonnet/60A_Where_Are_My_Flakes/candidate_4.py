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
    open_boxes = set(range(1, n + 1))
    for side, index in hints:
        if side == "left":
            open_boxes -= set(range(index, n + 1))
        else:
            open_boxes -= set(range(1, index + 1))
    if not open_boxes:
        return -1
    return len(open_boxes)


# --- clause: main :: () -> None ---
def main():
    n, hints = read_input()
    sys.stdout.write("%d\n" % count_boxes(n, hints))


if __name__ == "__main__":
    main()
