# CLAUSE: setup_environment
import sys
import heapq

INF = 10 ** 30

class ShortestPath:
    def __init__(self, n, graph, source):
        self.dist = [INF] * (n + 1)
        self.parent = [0] * (n + 1)
        self.edge = [-1] * (n + 1)
        self.dist[source] = 0
        pq = [(0, source)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != self.dist[u]:
                continue
            for v, w, eid in graph[u]:
                nd = d + w
                if nd < self.dist[v]:
                    self.dist[v] = nd
                    self.parent[v] = u
                    self.edge[v] = eid
                    heapq.heappush(pq, (nd, v))

def collect_path(tree, finish):
    nodes = []
    edges = []
    u = finish
    while u != 1:
        nodes.append(u)
        edges.append(tree.edge[u])
        u = tree.parent[u]
    nodes.append(1)
    nodes.reverse()
    edges.reverse()
    return nodes, edges

def make_component_ids(n, edges, parent_edge, roots, banned):
    nexts = [[] for _ in range(n + 1)]
    for x in range(1, n + 1):
        eid = parent_edge[x]
        if eid >= 0:
            a, b, _ = edges[eid]
            y = a ^ b ^ x
            nexts[x].append((y, eid))
            nexts[y].append((x, eid))
    comp = [-1] * (n + 1)
    for index, root in enumerate(roots):
        if comp[root] != -1:
            continue
        comp[root] = index
        stack = [root]
        while stack:
            u = stack.pop()
            for v, eid in nexts[u]:
                if eid in banned or comp[v] != -1:
                    continue
                comp[v] = index
                stack.append(v)
    return comp

# CLAUSE: solve_logic
def main():
    it = iter(sys.stdin.buffer.read().split())
    n = int(next(it))
    m = int(next(it))
    q = int(next(it))

    edges = []
    graph = [[] for _ in range(n + 1)]
    for eid in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        graph[u].append((v, w, eid))
        graph[v].append((u, w, eid))

    forward = ShortestPath(n, graph, 1)
    backward = ShortestPath(n, graph, n)
    path_nodes, path_edges = collect_path(forward, n)

    where = {}
    banned = set()
    for i, eid in enumerate(path_edges):
        where[eid] = i
        banned.add(eid)
        backward.parent[path_nodes[i]] = path_nodes[i + 1]
        backward.edge[path_nodes[i]] = eid

    left_comp = make_component_ids(n, edges, forward.edge, path_nodes, banned)
    right_comp = make_component_ids(n, edges, backward.edge, path_nodes, banned)

    k = len(path_edges)
    size = 1 << ((k - 1).bit_length())
    bucket = [INF] * (size * 2)

    for eid, edge in enumerate(edges):
        if eid in banned:
            continue
        u, v, w = edge
        variants = (
            (left_comp[u], right_comp[v], forward.dist[u] + w + backward.dist[v]),
            (left_comp[v], right_comp[u], forward.dist[v] + w + backward.dist[u]),
        )
        for l, r, value in variants:
            r -= 1
            if l > r:
                continue
            l += size
            r += size
            while l <= r:
                if l & 1:
                    bucket[l] = min(bucket[l], value)
                    l += 1
                if (r & 1) == 0:
                    bucket[r] = min(bucket[r], value)
                    r -= 1
                l >>= 1
                r >>= 1

    bypass = []
    for i in range(k):
        p = i + size
        value = INF
        while p:
            value = min(value, bucket[p])
            p >>= 1
        bypass.append(value)

    base = forward.dist[n]
    answer = []
    for _ in range(q):
        eid = int(next(it)) - 1
        x = int(next(it))
        u, v, _ = edges[eid]
        changed = min(forward.dist[u] + x + backward.dist[v], forward.dist[v] + x + backward.dist[u])
        if eid in where:
            answer.append(str(min(changed, bypass[where[eid]])))
        else:
            answer.append(str(min(changed, base)))

    sys.stdout.write("\n".join(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
