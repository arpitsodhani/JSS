import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause build_graph [Confidence: 1.00]
def build_graph(k):
    if k % 2 == 0:
        return None
    extent = 2 * k - 1
    edges = [(1, extent + 1)]
    for side in (0, extent):
        hub = side + 1
        lead = [side + 2 + i for i in range(k - 1)]
        next_value = [side + 1 + k + i for i in range(k - 1)]
        for v in lead:
            edges.append((hub, v))
            for u in next_value:
                edges.append((v, u))
        for i in range(0, k - 1, 2):
            edges.append((next_value[i], next_value[i + 1]))
    return edges

# Clause main [Confidence: 1.00]
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

