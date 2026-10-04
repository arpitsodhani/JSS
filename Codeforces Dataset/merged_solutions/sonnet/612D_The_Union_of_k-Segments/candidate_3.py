import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    k = fields[1]
    pieces = []
    for i in range(n):
        pieces.append((fields[2 + 2 * i], fields[3 + 2 * i]))
    return k, pieces


# --- clause: merge_cover :: (k: int, pieces: list[tuple[int, int]]) -> list[tuple[int, int]] ---
def merge_cover(k, pieces):
    events = []
    for first_side, right in pieces:
        events.append((first_side, 0))
        events.append((right, 1))
    events.sort()
    covered = 0
    opening = 0
    out = []
    for point, kind in events:
        if kind == 0:
            covered += 1
            if covered == k:
                opening = point
        else:
            if covered == k:
                out.append((opening, point))
            covered -= 1
    return out


# --- clause: main :: () -> None ---
def main():
    k, pieces = read_input()
    spans = merge_cover(k, pieces)
    out = [str(len(spans))]
    for first_side, right in spans:
        out.append("%d %d" % (first_side, right))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
