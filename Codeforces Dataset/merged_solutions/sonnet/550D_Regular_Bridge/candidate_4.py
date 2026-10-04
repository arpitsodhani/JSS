import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: build_graph :: (k: int) -> list[tuple[int, int]] | None ---
def build_graph(k):
    if k % 2 == 0:
        return None
    half = 2 * k - 1
    edges = []
    for shift in (0, half):
        hub = shift + 1
        inner = []
        outer = []
        for i in range(k - 1):
            inner.append(shift + 2 + i)
            outer.append(shift + k + 1 + i)
        for v in inner:
            edges.append((hub, v))
        for v in inner:
            for u in outer:
                edges.append((v, u))
        spot = 0
        while spot + 1 < len(outer):
            edges.append((outer[spot], outer[spot + 1]))
            spot += 2
    edges.append((1, half + 1))
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
