import sys


# --- clause: read_input :: () -> list[tuple[int, list[tuple[int, int]]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        m = fields[offset + 1]
        offset += 2
        tracks = []
        for _ in range(m):
            tracks.append((fields[offset], fields[offset + 1]))
            offset += 2
        cases.append((n, tracks))
    return cases


# --- clause: pick_closures :: (n: int, tracks: list[tuple[int, int]]) -> list[int] ---
def pick_closures(n, tracks):
    down = [[] for _ in range(n + 1)]
    for x, y in tracks:
        down[x].append(y)
    level = [0] * (n + 1)
    closed = []
    for v in range(1, n + 1):
        if level[v] == 2:
            closed.append(v)
            continue
        for u in down[v]:
            if level[v] + 1 > level[u]:
                level[u] = level[v] + 1
    return closed


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n, tracks in read_input():
        closed = pick_closures(n, tracks)
        pieces.append(str(len(closed)))
        pieces.append(" ".join(map(str, closed)))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
