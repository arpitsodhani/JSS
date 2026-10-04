import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int, int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    links = []
    pos = 2
    while len(links) < m:
        f = int(data[pos])
        t = int(data[pos + 1])
        w = int(data[pos + 2])
        b = int(data[pos + 3])
        pos += 4
        links.append((f, t, w, b))
    return n, m, links


# --- clause: find_root :: (parent: list[int], offset: list[int], x: int) -> tuple[int, int] ---
def find_root(parent, offset, x):
    root = x
    acc = 0
    while parent[root] != root:
        acc += offset[root]
        root = parent[root]
    node = x
    rel = acc
    while node != parent[node]:
        step = parent[node]
        carried = rel - offset[node]
        parent[node] = root
        offset[node] = rel
        node = step
        rel = carried
    return root, acc


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
    for index in range(m):
        f, t, w, b = links[index]
        drop = 2 * w * b
        rf, pf = find_root(parent, offset, f)
        rt, pt = find_root(parent, offset, t)
        if rf == rt:
            if pf - pt != drop:
                return "BAD " + str(index + 1)
        else:
            shift = pf - pt - drop
            if size[rf] < size[rt]:
                rf, rt = rt, rf
                shift = -shift
            parent[rt] = rf
            offset[rt] = shift
            size[rf] += size[rt]
            top = high[rt] + shift
            if top > high[rf]:
                high[rf] = top
                high_count[rf] = high_count[rt]
            elif top == high[rf]:
                high_count[rf] += high_count[rt]
            bottom = low[rt] + shift
            if bottom < low[rf]:
                low[rf] = bottom
                low_count[rf] = low_count[rt]
            elif bottom == low[rf]:
                low_count[rf] += low_count[rt]
        source, source_p = find_root(parent, offset, 1)
        sink, sink_p = find_root(parent, offset, n)
        if high[source] != source_p or high_count[source] != 1:
            return "BAD " + str(index + 1)
        if low[sink] != sink_p or low_count[sink] != 1:
            return "BAD " + str(index + 1)
        if source == sink:
            if not joined:
                joined = True
                span = source_p - sink_p
                for node in range(1, n + 1):
                    root, _ = find_root(parent, offset, node)
                    if root != source and high[root] - low[root] >= span:
                        return "BAD " + str(index + 1)
            else:
                root, _ = find_root(parent, offset, f)
                if root != source and high[root] - low[root] >= span:
                    return "BAD " + str(index + 1)
    source, source_p = find_root(parent, offset, 1)
    sink, sink_p = find_root(parent, offset, n)
    if source != sink:
        return "UNKNOWN"
    return str((source_p - sink_p) // 2)


# --- clause: main :: () -> None ---
def main():
    n, m, links = read_input()
    print(evaluate_links(n, m, links))


if __name__ == "__main__":
    main()
