import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: build_graph :: (k: int) -> list[tuple[int, int]] | None ---
def build_graph(k):
    if k % 2 == 0:
        return None
    width = 2 * k - 1
    edges = [(1, width + 1)]
    for side in (0, width):
        hub = side + 1
        first = [side + 2 + i for i in range(k - 1)]
        two = [side + 1 + k + i for i in range(k - 1)]
        for v in first:
            edges.append((hub, v))
            for u in two:
                edges.append((v, u))
        for i in range(0, k - 1, 2):
            edges.append((two[i], two[i + 1]))
    return edges


# --- clause: main :: () -> None ---
def main():
    k = read_input()
    edges = build_graph(k)
    if edges is None:
        sys.stdout.write("NO\n")
        return
    spots = set()
    for u, v in edges:
        spots.add(u)
        spots.add(v)
    out = ["YES", "%d %d" % (len(spots), len(edges))]
    for u, v in edges:
        out.append("%d %d" % (u, v))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
