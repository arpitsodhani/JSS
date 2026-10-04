# CLAUSE: setup_environment
import sys

def main():
    buf = sys.stdin.buffer.read().split()
    if not buf:
        return
    n = int(buf[0])
    m = int(buf[1])
    all_edges = []
    k = 2
    for edge_id in range(m):
        x = int(buf[k])
        y = int(buf[k + 1])
        z = int(buf[k + 2])
        k += 3
        all_edges.append((z, x, y, edge_id))

# CLAUSE: solve_logic
    base = list(range(n + 1))
    cnt = [1] * (n + 1)

    def find_base(x):
        while base[x] != x:
            base[x] = base[base[x]]
            x = base[x]
        return x

    is_tree = [False] * m
    graph = [[] for _ in range(n + 1)]
    sorted_edges = sorted(all_edges)
    for w, u, v, eid in sorted_edges:
        ru = find_base(u)
        rv = find_base(v)
        if ru == rv:
            continue
        if cnt[ru] < cnt[rv]:
            ru, rv = rv, ru
        base[rv] = ru
        cnt[ru] += cnt[rv]
        is_tree[eid] = True
        graph[u].append((v, w, eid))
        graph[v].append((u, w, eid))

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    par_edge = [-1] * (n + 1)
    par_w = [0] * (n + 1)
    stack = [(1, 0, 0, -1)]
    while stack:
        v, p, w, eid = stack.pop()
        parent[v] = p
        par_w[v] = w
        par_edge[v] = eid
        for to, tw, te in graph[v]:
            if to != p:
                depth[to] = depth[v] + 1
                stack.append((to, v, tw, te))

    lim = (n + 1).bit_length()
    lift = [parent]
    lift_max = [par_w]
    for j in range(1, lim):
        before = lift[j - 1]
        before_max = lift_max[j - 1]
        now = [0] * (n + 1)
        now_max = [0] * (n + 1)
        for v in range(1, n + 1):
            mid = before[v]
            now[v] = before[mid]
            now_max[v] = max(before_max[v], before_max[mid])
        lift.append(now)
        lift_max.append(now_max)

    def strongest(u, v):
        best = 0
        if depth[u] < depth[v]:
            u, v = v, u
        d = depth[u] - depth[v]
        for bit, row in enumerate(lift):
            if d >> bit & 1:
                val = lift_max[bit][u]
                if val > best:
                    best = val
                u = row[u]
        if u == v:
            return best
        for bit in range(lim - 1, -1, -1):
            if lift[bit][u] != lift[bit][v]:
                best = max(best, lift_max[bit][u], lift_max[bit][v])
                u = lift[bit][u]
                v = lift[bit][v]
        return max(best, lift_max[0][u], lift_max[0][v])

    result = [-1] * m
    other_edges = []
    for w, u, v, eid in all_edges:
        if is_tree[eid]:
            continue
        result[eid] = strongest(u, v) - 1
        other_edges.append((w, u, v))

    next_node = list(range(n + 1))

    def head(x):
        while next_node[x] != x:
            next_node[x] = next_node[next_node[x]]
            x = next_node[x]
        return x

    for w, u, v in sorted(other_edges):
        u = head(u)
        v = head(v)
        while u != v:
            if depth[u] < depth[v]:
                u, v = v, u
            result[par_edge[u]] = w - 1
            next_node[u] = head(parent[u])
            u = head(u)

# CLAUSE: finish_program
    sys.stdout.write(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
