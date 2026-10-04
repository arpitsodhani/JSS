import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    k = raw[1]
    pieces = []
    for i in range(n):
        pieces.append((raw[2 + 2 * i], raw[3 + 2 * i]))
    return k, pieces


# --- clause: merge_cover :: (k: int, pieces: list[tuple[int, int]]) -> list[tuple[int, int]] ---
def merge_cover(k, pieces):
    events = []
    for low, right in pieces:
        events.append((low, 0))
        events.append((right, 1))
    events.sort()
    covered = 0
    head_pos = 0
    out = []
    for point, kind in events:
        if kind == 0:
            covered += 1
            if covered == k:
                head_pos = point
        else:
            if covered == k:
                out.append((head_pos, point))
            covered -= 1
    return out


# --- clause: main :: () -> None ---
def main():
    k, pieces = read_input()
    spans = merge_cover(k, pieces)
    out = [str(len(spans))]
    for low, right in spans:
        out.append("%d %d" % (low, right))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
