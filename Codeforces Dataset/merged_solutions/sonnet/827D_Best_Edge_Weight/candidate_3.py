# CLAUSE: setup_environment
import sys
from collections import deque

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    it = iter(raw)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for idx in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append({"u": u, "v": v, "w": w, "id": idx})

# CLAUSE: solve_logic
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(v):
        r = v
        while parent[r] != r:
            r = parent[r]
        while parent[v] != v:
            nxt = parent[v]
            parent[v] = r
            v = nxt
        return r

    chosen = [False] * m
    g = [[] for _ in range(n + 1)]
    for e in sorted(edges, key=lambda z: z["w"]):
        a = find(e["u"])
        b = find(e["v"])
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            chosen[e["id"]] = True
            g[e["u"]].append((e["v"], e["w"], e["id"]))
            g[e["v"]].append((e["u"], e["w"], e["id"]))

    levels = max(1, n.bit_length())
    anc = [[0] * (n + 1) for _ in range(levels)]
    high = [[0] * (n + 1) for _ in range(levels)]
    dep = [-1] * (n + 1)
    via = [-1] * (n + 1)
    dep[1] = 0
    q = deque([1])
    while q:
        v = q.popleft()
        for to, wt, eid in g[v]:
            if dep[to] == -1:
                dep[to] = dep[v] + 1
                anc[0][to] = v
                high[0][to] = wt
                via[to] = eid
                q.append(to)

    for k in range(1, levels):
        prev_a = anc[k - 1]
        prev_h = high[k - 1]
        cur_a = anc[k]
        cur_h = high[k]
        for v in range(1, n + 1):
            z = prev_a[v]
            cur_a[v] = prev_a[z]
            cur_h[v] = prev_h[v] if prev_h[v] >= prev_h[z] else prev_h[z]

    def path_max(u, v):
        best = 0
        if dep[u] > dep[v]:
            deep, shallow = u, v
        else:
            deep, shallow = v, u
        delta = dep[deep] - dep[shallow]
        k = 0
        while delta:
            if delta & 1:
                if high[k][deep] > best:
                    best = high[k][deep]
                deep = anc[k][deep]
            delta >>= 1
            k += 1
        u, v = deep, shallow
        if u == v:
            return best
        for k in range(levels - 1, -1, -1):
            if anc[k][u] != anc[k][v]:
                best = max(best, high[k][u], high[k][v])
                u = anc[k][u]
                v = anc[k][v]
        return max(best, high[0][u], high[0][v])

    out = [-1] * m
    nxt = list(range(n + 1))

    def get(v):
        while nxt[v] != v:
            nxt[v] = nxt[nxt[v]]
            v = nxt[v]
        return v

    for e in edges:
        if not chosen[e["id"]]:
            out[e["id"]] = path_max(e["u"], e["v"]) - 1

    for e in sorted((x for x in edges if not chosen[x["id"]]), key=lambda z: z["w"]):
        u = get(e["u"])
        v = get(e["v"])
        while u != v:
            if dep[u] < dep[v]:
                u, v = v, u
            out[via[u]] = e["w"] - 1
            nxt[u] = get(anc[0][u])
            u = get(u)

# CLAUSE: finish_program
    print(*out)

if __name__ == "__main__":
    main()
