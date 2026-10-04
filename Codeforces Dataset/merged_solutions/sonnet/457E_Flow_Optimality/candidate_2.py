import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int, int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    links = []
    idx = 2
    for _ in range(m):
        f, t = int(data[idx]), int(data[idx + 1])
        w, b = int(data[idx + 2]), int(data[idx + 3])
        idx += 4
        links.append((f, t, w, b))
    return n, m, links


# --- clause: find_root :: (parent: list[int], offset: list[int], x: int) -> tuple[int, int] ---
def find_root(parent, offset, x):
    root = x
    total = 0
    while parent[root] != root:
        total += offset[root]
        root = parent[root]
    node = x
    rel = total
    while parent[node] != node:
        nxt = parent[node]
        nxt_rel = rel - offset[node]
        parent[node] = root
        offset[node] = rel
        node = nxt
        rel = nxt_rel
    return root, total


# --- clause: evaluate_links :: (n: int, m: int, links: list[tuple[int, int, int, int]]) -> str ---
def evaluate_links(n, m, links):
    parent = list(range(n + 1))
    offset = [0] * (n + 1)
    size = [1] * (n + 1)
    high = [0] * (n + 1)
    high_count = [1] * (n + 1)
    low = [0] * (n + 1)
    low_count = [1] * (n + 1)
    joined = False
    span = 0
    for index, link in enumerate(links):
        f, t, w, b = link
        drop = 2 * w * b
        rf, pf = find_root(parent, offset, f)
        rt, pt = find_root(parent, offset, t)
        if rf == rt:
            if pf - pt != drop:
                return "BAD %d" % (index + 1)
        else:
            shift = pf - pt - drop
            if size[rf] < size[rt]:
                rf, rt = rt, rf
                shift = -shift
            parent[rt] = rf
            offset[rt] = shift
            size[rf] += size[rt]
            top = high[rt] + shift
            if high[rf] < top:
                high[rf] = top
                high_count[rf] = high_count[rt]
            elif top == high[rf]:
                high_count[rf] += high_count[rt]
            bottom = low[rt] + shift
            if low[rf] > bottom:
                low[rf] = bottom
                low_count[rf] = low_count[rt]
            elif bottom == low[rf]:
                low_count[rf] += low_count[rt]
        source, source_p = find_root(parent, offset, 1)
        sink, sink_p = find_root(parent, offset, n)
        if high[source] != source_p or high_count[source] != 1:
            return "BAD %d" % (index + 1)
        if low[sink] != sink_p or low_count[sink] != 1:
            return "BAD %d" % (index + 1)
        if source == sink:
            if not joined:
                joined = True
                span = source_p - sink_p
                for node in range(1, n + 1):
                    root, _ = find_root(parent, offset, node)
                    if root != source and high[root] - low[root] >= span:
                        return "BAD %d" % (index + 1)
            else:
                root, _ = find_root(parent, offset, f)
                if root != source and high[root] - low[root] >= span:
                    return "BAD %d" % (index + 1)
    source, source_p = find_root(parent, offset, 1)
    sink, sink_p = find_root(parent, offset, n)
    if source != sink:
        return "UNKNOWN"
    return str((source_p - sink_p) // 2)


# --- clause: main :: () -> None ---
def main():
    n, m, links = read_input()
    sys.stdout.write("%s\n" % evaluate_links(n, m, links))


if __name__ == "__main__":
    main()
