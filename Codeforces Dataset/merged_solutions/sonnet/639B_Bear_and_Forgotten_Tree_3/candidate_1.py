import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1]), int(data[2])


# --- clause: build_tree :: (n: int, d: int, h: int) -> list[str] ---
def build_tree(n, d, h):
    if d > 2 * h:
        return None
    edges = []
    for step in range(1, h + 1):
        edges.append("%d %d" % (step, step + 1))
    nxt = h + 2
    previous = 1
    for _ in range(d - h):
        edges.append("%d %d" % (previous, nxt))
        previous = nxt
        nxt += 1
    while nxt <= n:
        if d == h:
            if h < 2:
                return None
            edges.append("%d %d" % (2, nxt))
        else:
            edges.append("%d %d" % (1, nxt))
        nxt += 1
    return edges


# --- clause: main :: () -> None ---
def main():
    n, d, h = read_input()
    edges = build_tree(n, d, h)
    if edges is None:
        sys.stdout.write("-1\n")
        return
    sys.stdout.write("\n".join(edges) + "\n")


if __name__ == "__main__":
    main()
