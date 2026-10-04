# CLAUSE: setup_environment
import sys
from heapq import heappop, heappush

INF = 10 ** 30

def dijkstra(source, graph, n):
    dist = [INF] * (n + 1)
    par = [0] * (n + 1)
    pedge = [-1] * (n + 1)
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heappop(heap)
        if d != dist[u]:
            continue
        for v, w, eid in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                par[v] = u
                pedge[v] = eid
                heappush(heap, (nd, v))
    return dist, par, pedge

def components(n, edges, parent_edge, roots, blocked):
    tree = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        eid = parent_edge[v]
        if eid != -1:
            a, b, _ = edges[eid]
            p = a ^ b ^ v
            tree[v].append((p, eid))
            tree[p].append((v, eid))
    comp = [-1] * (n + 1)
    for i, root in enumerate(roots):
        comp[root] = i
        stack = [root]
        while stack:
            u = stack.pop()
            for v, eid in tree[u]:
                if eid in blocked or comp[v] != -1:
                    continue
                comp[v] = i
                stack.append(v)
    return comp

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    n, m, q = data[at], data[at + 1], data[at + 2]
    at += 3
    edges = []
    graph = [[] for _ in range(n + 1)]
    for eid in range(m):
        u, v, w = data[at], data[at + 1], data[at + 2]
        at += 3
        edges.append((u, v, w))
        graph[u].append((v, w, eid))
        graph[v].append((u, w, eid))

    d1, p1, e1 = dijkstra(1, graph, n)
    dn, pn, en = dijkstra(n, graph, n)
    base = d1[n]

    nodes = []
    path_edges = []
    cur = n
    while cur != 1:
        nodes.append(cur)
        path_edges.append(e1[cur])
        cur = p1[cur]
    nodes.append(1)
    nodes.reverse()
    path_edges.reverse()

    pos = {eid: i for i, eid in enumerate(path_edges)}
    blocked = set(path_edges)
    k = len(path_edges)

    for i, eid in enumerate(path_edges):
        pn[nodes[i]] = nodes[i + 1]
        en[nodes[i]] = eid

    c1 = components(n, edges, e1, nodes, blocked)
    cn = components(n, edges, en, nodes, blocked)

    size = 1
    while size < k:
        size <<= 1
    seg = [INF] * (size << 1)

    def apply(l, r, val):
        l += size
        r += size
        while l <= r:
            if l & 1:
                if val < seg[l]:
                    seg[l] = val
                l += 1
            if not (r & 1):
                if val < seg[r]:
                    seg[r] = val
                r -= 1
            l >>= 1
            r >>= 1

    for eid, (u, v, w) in enumerate(edges):
        if eid in pos:
            continue
        a, b = c1[u], cn[v]
        if a < b:
            apply(a, b - 1, d1[u] + w + dn[v])
        a, b = c1[v], cn[u]
        if a < b:
            apply(a, b - 1, d1[v] + w + dn[u])

    avoid = [INF] * k
    for i in range(k):
        x = i + size
        best = INF
        while x:
            if seg[x] < best:
                best = seg[x]
            x >>= 1
        avoid[i] = best

    out = []
    for _ in range(q):
        eid = data[at] - 1
        x = data[at + 1]
        at += 2
        u, v, _ = edges[eid]
        changed = min(d1[u] + x + dn[v], d1[v] + x + dn[u])
        if eid in pos:
            out.append(str(min(avoid[pos[eid]], changed)))
        else:
            out.append(str(min(base, changed)))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
