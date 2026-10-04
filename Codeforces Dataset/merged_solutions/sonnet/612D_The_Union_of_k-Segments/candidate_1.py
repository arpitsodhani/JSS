import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    pieces = []
    for i in range(n):
        pieces.append((data[2 + 2 * i], data[3 + 2 * i]))
    return k, pieces


# --- clause: merge_cover :: (k: int, pieces: list[tuple[int, int]]) -> list[tuple[int, int]] ---
def merge_cover(k, pieces):
    events = []
    for left, right in pieces:
        events.append((left, 0))
        events.append((right, 1))
    events.sort()
    covered = 0
    start = 0
    out = []
    for point, kind in events:
        if kind == 0:
            covered += 1
            if covered == k:
                start = point
        else:
            if covered == k:
                out.append((start, point))
            covered -= 1
    return out


# --- clause: main :: () -> None ---
def main():
    k, pieces = read_input()
    spans = merge_cover(k, pieces)
    out = [str(len(spans))]
    for left, right in spans:
        out.append("%d %d" % (left, right))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
