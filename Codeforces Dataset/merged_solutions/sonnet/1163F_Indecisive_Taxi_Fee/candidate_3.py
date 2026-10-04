# CLAUSE: setup_environment
import sys
import heapq

INF = 10 ** 30

def shortest_tree(start, adj, n):
    dist = [INF] * (n + 1)
    parent = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        du, u = heapq.heappop(pq)
        if du > dist[u]:
            continue
        for v, w, eid in adj[u]:
            nd = du + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                parent_edge[v] = eid
                heapq.heappush(pq, (nd, v))
    return dist, parent, parent_edge

def split_by_path(n, edges, tree_edge, path_nodes, is_path_edge):
    around = [[] for _ in range(n + 1)]
    for node in range(1, n + 1):
        eid = tree_edge[node]
        if eid >= 0:
            u, v, _ = edges[eid]
            other = u ^ v ^ node
            around[node].append((other, eid))
            around[other].append((node, eid))
    comp = [-1] * (n + 1)
    for root_index, root in enumerate(path_nodes):
        comp[root] = root_index
    stack = path_nodes[:]
    while stack:
        u = stack.pop()
        cu = comp[u]
        for v, eid in around[u]:
            if is_path_edge[eid] or comp[v] != -1:
                continue
            comp[v] = cu
            stack.append(v)
    return comp

def range_push(tree, size, left, right, value):
    left += size
    right += size
    while left <= right:
        if left & 1:
            tree[left] = min(tree[left], value)
            left += 1
        if right & 1 == 0:
            tree[right] = min(tree[right], value)
            right -= 1
        left >>= 1
        right >>= 1

def point_values(tree, size, count):
    ans = [INF] * count
    for i in range(count):
        p = i + size
        while p:
            ans[i] = min(ans[i], tree[p])
            p >>= 1
    return ans

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    ptr = 0
    n = int(raw[ptr])
    m = int(raw[ptr + 1])
    q = int(raw[ptr + 2])
    ptr += 3

    edges = [None] * m
    adj = [[] for _ in range(n + 1)]
    for eid in range(m):
        u = int(raw[ptr])
        v = int(raw[ptr + 1])
        w = int(raw[ptr + 2])
        ptr += 3
        edges[eid] = (u, v, w)
        adj[u].append((v, w, eid))
        adj[v].append((u, w, eid))

    from_one, par_one, edge_one = shortest_tree(1, adj, n)
    from_n, par_n, edge_n = shortest_tree(n, adj, n)

    path_nodes = []
    path_edges = []
    x = n
    while x != 1:
        path_nodes.append(x)
        path_edges.append(edge_one[x])
        x = par_one[x]
    path_nodes.append(1)
    path_nodes = path_nodes[::-1]
    path_edges = path_edges[::-1]

    k = len(path_edges)
    path_index = {}
    is_path = [False] * m
    for i, eid in enumerate(path_edges):
        path_index[eid] = i
        is_path[eid] = True
        par_n[path_nodes[i]] = path_nodes[i + 1]
        edge_n[path_nodes[i]] = eid

    comp_one = split_by_path(n, edges, edge_one, path_nodes, is_path)
    comp_n = split_by_path(n, edges, edge_n, path_nodes, is_path)

    size = 1
    while size < k:
        size *= 2
    lazy_min = [INF] * (size * 2)

    for eid in range(m):
        if is_path[eid]:
            continue
        u, v, w = edges[eid]
        a = comp_one[u]
        b = comp_n[v]
        if a < b:
            range_push(lazy_min, size, a, b - 1, from_one[u] + w + from_n[v])
        a = comp_one[v]
        b = comp_n[u]
        if a < b:
            range_push(lazy_min, size, a, b - 1, from_one[v] + w + from_n[u])

    replacement = point_values(lazy_min, size, k)
    original = from_one[n]
    answers = []

    for _ in range(q):
        eid = int(raw[ptr]) - 1
        new_w = int(raw[ptr + 1])
        ptr += 2
        u, v, _ = edges[eid]
        through = min(from_one[u] + new_w + from_n[v], from_one[v] + new_w + from_n[u])
        if eid in path_index:
            answers.append(str(min(replacement[path_index[eid]], through)))
        else:
            answers.append(str(min(original, through)))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
main()
