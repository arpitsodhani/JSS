import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    links = []
    pos = 2
    for _ in range(m):
        f = int(data[pos])
        t = int(data[pos + 1])
        w = int(data[pos + 2])
        b = int(data[pos + 3])
        pos += 4
        links.append((f, t, w, b))
    return n, m, links

# Clause find_root [Confidence: 1.00]
def find_root(parent, offset, x):
    root = x
    acc = 0
    while parent[root] != root:
        acc += offset[root]
        root = parent[root]
    node = x
    rel = acc
    while parent[node] != node:
        nxt = parent[node]
        nxt_rel = rel - offset[node]
        parent[node] = root
        offset[node] = rel
        node = nxt
        rel = nxt_rel
    return root, acc

# Clause evaluate_links [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    n, m, links = read_input()
    sys.stdout.write(evaluate_links(n, m, links) + "\n")


if __name__ == "__main__":
    main()

