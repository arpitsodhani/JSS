# CLAUSE: setup_environment
import sys
from heapq import heappop, heappush

INF = 10 ** 30

def run_dijkstra(start, graph, n):
    d = [INF] * (n + 1)
    p = [0] * (n + 1)
    pe = [-1] * (n + 1)
    d[start] = 0
    heap = [(0, start)]
    while heap:
        cost, node = heappop(heap)
        if cost != d[node]:
            continue
        for to, weight, eid in graph[node]:
            nc = cost + weight
            if nc < d[to]:
                d[to] = nc
                p[to] = node
                pe[to] = eid
                heappush(heap, (nc, to))
    return d, p, pe

def mark_parts(n, edges, parent_edge, roots, path_set):
    tree = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        eid = parent_edge[v]
        if eid == -1:
            continue
        a, b, _ = edges[eid]
        u = a ^ b ^ v
        tree[u].append((v, eid))
        tree[v].append((u, eid))
    part = [-1] * (n + 1)
    for i in range(len(roots)):
        root = roots[i]
        part[root] = i
        stack = [root]
        while stack:
            u = stack.pop()
            for v, eid in tree[u]:
                if eid not in path_set and part[v] < 0:
                    part[v] = i
                    stack.append(v)
    return part

# CLAUSE: solve_logic
def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    t = 0
    n, m, q = nums[t], nums[t + 1], nums[t + 2]
    t += 3
    edges = []
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = nums[t], nums[t + 1], nums[t + 2]
        t += 3
        edges.append((u, v, w))
        graph[u].append((v, w, i))
        graph[v].append((u, w, i))

    ds, ps, pes = run_dijkstra(1, graph, n)
    dt, pt, pet = run_dijkstra(n, graph, n)

    nodes = []
    ep = []
    v = n
    while v != 1:
        nodes.append(v)
        ep.append(pes[v])
        v = ps[v]
    nodes.append(1)
    nodes.reverse()
    ep.reverse()

    loc = {}
    path_set = set()
    for i, eid in enumerate(ep):
        loc[eid] = i
        path_set.add(eid)
        pt[nodes[i]] = nodes[i + 1]
        pet[nodes[i]] = eid

    cs = mark_parts(n, edges, pes, nodes, path_set)
    ct = mark_parts(n, edges, pet, nodes, path_set)

    k = len(ep)
    starts = [[] for _ in range(k)]
    for eid, (u, v, w) in enumerate(edges):
        if eid in path_set:
            continue
        a = cs[u]
        b = ct[v]
        if a < b:
            starts[a].append((ds[u] + w + dt[v], b - 1))
        a = cs[v]
        b = ct[u]
        if a < b:
            starts[a].append((ds[v] + w + dt[u], b - 1))

    avoid = [INF] * k
    live = []
    for i in range(k):
        for item in starts[i]:
            heappush(live, item)
        while live and live[0][1] < i:
            heappop(live)
        if live:
            avoid[i] = live[0][0]

    base = ds[n]
    res = []
    for _ in range(q):
        eid = nums[t] - 1
        x = nums[t + 1]
        t += 2
        u, v, _ = edges[eid]
        changed = ds[u] + x + dt[v]
        other = ds[v] + x + dt[u]
        if other < changed:
            changed = other
        if eid in loc:
            ans = avoid[loc[eid]]
            if changed < ans:
                ans = changed
        else:
            ans = base
            if changed < ans:
                ans = changed
        res.append(str(ans))

    print("\n".join(res))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
