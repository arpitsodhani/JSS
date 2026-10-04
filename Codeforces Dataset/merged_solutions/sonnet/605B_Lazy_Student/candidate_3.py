import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    edges = []
    pos = 2
    while len(edges) < m:
        edges.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    return n, m, edges


# --- clause: order_edges :: (m: int, edges: list[tuple[int, int]]) -> list[int] ---
def order_edges(m, edges):
    return sorted(range(m), key=lambda i: (edges[i][0], -edges[i][1]))


# --- clause: assign_ends :: (n: int, m: int, edges: list[tuple[int, int]], order: list[int]) -> list ---
def assign_ends(n, m, edges, order):
    import heapq

    parent = list(range(n + 1))
    size = [1] * (n + 1)
    members = [[v] for v in range(n + 1)]
    cursor = [None] * (n + 1)
    used = set()

    def mark(u, v):
        key = (u, v) if u < v else (v, u)
        used.add(key)

    def is_used(u, v):
        key = (u, v) if u < v else (v, u)
        return key in used

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    heap = [(-1, v) for v in range(1, n + 1)]
    heapq.heapify(heap)

    def push_root(root):
        heapq.heappush(heap, (-size[root], root))

    def top_valid_root():
        while heap:
            neg_sz, r = heap[0]
            if find(r) == r and size[r] == -neg_sz:
                return r
            heapq.heappop(heap)
        return None

    def next_fresh_pair(root):
        L = members[root]
        c = cursor[root]
        j0, i0 = c[0], c[1]
        while j0 < len(L):
            if i0 > j0 - 2:
                j0 += 1
                i0 = 0
                continue
            u, v = L[i0], L[j0]
            i0 += 1
            if is_used(u, v):
                continue
            c[0], c[1] = j0, i0
            return u, v
        c[0], c[1] = j0, i0
        return None

    out = [None] * m
    i = 0
    while i < m:
        w = edges[order[i]][0]
        j = i
        tree_here = []
        nontree_here = []
        while j < m and edges[order[j]][0] == w:
            idx = order[j]
            (tree_here if edges[idx][1] == 1 else nontree_here).append(idx)
            j += 1

        for idx in tree_here:
            ra = top_valid_root()
            if ra is None:
                return None
            heapq.heappop(heap)
            rb = top_valid_root()
            if rb is None or rb == ra:
                return None
            heapq.heappop(heap)
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            tail_a = members[ra][-1]
            head_b = members[rb][0]
            out[idx] = (tail_a, head_b)
            mark(tail_a, head_b)
            members[ra].extend(members[rb])
            members[rb] = None
            parent[rb] = ra
            size[ra] += size[rb]
            if cursor[ra] is None:
                cursor[ra] = [2, 0]
            push_root(ra)

        for idx in nontree_here:
            r = top_valid_root()
            if r is None or size[r] < 2:
                return None
            pair = next_fresh_pair(r)
            if pair is None:
                return None
            out[idx] = pair
            mark(*pair)

        i = j

    r = top_valid_root()
    if r is None or size[r] != n:
        return None
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, edges = read_input()
    ends = assign_ends(n, m, edges, order_edges(m, edges))
    if ends is None:
        print(-1)
        return
    out = []
    for u, v in ends:
        out.append(str(u) + " " + str(v))
    print("\n".join(out))


if __name__ == "__main__":
    main()
