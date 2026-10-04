import sys


# --- clause: read_input :: () -> tuple[int, int, list, int, int, int, int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    edges = []
    pos = 2
    for _ in range(m):
        u = int(data[pos])
        pos += 1
        v = int(data[pos])
        pos += 1
        w = int(data[pos])
        pos += 1
        edges.append((u, v, w))
    p = int(data[pos])
    k = int(data[pos + 1])
    a = int(data[pos + 2])
    b = int(data[pos + 3])
    c = int(data[pos + 4])
    pos += 5
    first = [int(token) for token in data[pos:pos + p]]
    return n, m, edges, p, k, a, b, c, first


# --- clause: spanning_cost :: (n: int, edges: list[tuple[int, int, int]], x: int) -> tuple[int, int] ---
def spanning_cost(n, edges, x):
    edges_sorted = sorted(edges, key=lambda e: e[2])
    weights_sorted = [e[2] for e in edges_sorted]
    return _spanning_cost_core(n, edges_sorted, weights_sorted, x)


def _spanning_cost_core(n, edges_sorted, weights_sorted, x):
    import bisect

    m = len(edges_sorted)
    split = bisect.bisect_right(weights_sorted, x)
    li = split - 1
    ri = split
    parent = list(range(n + 1))
    slope = 0
    offset = 0
    used = 0
    while used < n - 1 and (li >= 0 or ri < m):
        if li < 0:
            u, v, w = edges_sorted[ri]
            ri += 1
        elif ri >= m:
            u, v, w = edges_sorted[li]
            li -= 1
        else:
            dl = x - weights_sorted[li]
            dr = weights_sorted[ri] - x
            if dl < dr:
                u, v, w = edges_sorted[li]
                li -= 1
            else:
                u, v, w = edges_sorted[ri]
                ri += 1
        ru = u
        while parent[ru] != ru:
            parent[ru] = parent[parent[ru]]
            ru = parent[ru]
        rv = v
        while parent[rv] != rv:
            parent[rv] = parent[parent[rv]]
            rv = parent[rv]
        if ru == rv:
            continue
        parent[ru] = rv
        used += 1
        if w <= x:
            slope += 1
            offset -= w
        else:
            slope -= 1
            offset += w
    return slope, offset


# --- clause: build_pieces :: (n: int, edges: list[tuple[int, int, int]]) -> tuple ---
def build_pieces(n, edges):
    marks = {0}
    for i in range(len(edges)):
        marks.add(edges[i][2])
        for j in range(i + 1, len(edges)):
            marks.add((edges[i][2] + edges[j][2] + 1) // 2)
    points = sorted(marks)

    edges_sorted = sorted(edges, key=lambda e: e[2])
    weights_sorted = [e[2] for e in edges_sorted]

    slopes = []
    offsets = []
    for x in points:
        slope, offset = _spanning_cost_core(n, edges_sorted, weights_sorted, x)
        slopes.append(slope)
        offsets.append(offset)
    return points, slopes, offsets


# --- clause: answer_queries :: (points: list[int], slopes: list[int], offsets: list[int], p: int, k: int, a: int, b: int, c: int, first: list[int]) -> int ---
def answer_queries(points, slopes, offsets, p, k, a, b, c, first):
    import bisect

    br = bisect.bisect_right
    total = 0
    query = 0
    step = 0
    while step < p:
        query = first[step]
        idx = br(points, query) - 1
        total ^= slopes[idx] * query + offsets[idx]
        step += 1
    while step < k:
        query = (query * a + b) % c
        idx = br(points, query) - 1
        total ^= slopes[idx] * query + offsets[idx]
        step += 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, m, edges, p, k, a, b, c, first = read_input()
    points, slopes, offsets = build_pieces(n, edges)
    sys.stdout.write(str(answer_queries(points, slopes, offsets, p, k, a, b, c, first)) + "\n")


if __name__ == "__main__":
    main()
