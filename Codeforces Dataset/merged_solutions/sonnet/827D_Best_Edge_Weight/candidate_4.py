# CLAUSE: setup_environment
import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    m = int(tokens[1])
    edges = []
    pos = 2
    for eid in range(m):
        a = int(tokens[pos])
        b = int(tokens[pos + 1])
        c = int(tokens[pos + 2])
        pos += 3
        edges.append((c, a, b, eid))

# CLAUSE: solve_logic
    comp = list(range(n + 1))
    weight = [1] * (n + 1)

    def leader(x):
        while comp[x] != x:
            comp[x] = comp[comp[x]]
            x = comp[x]
        return x

    mst = [False] * m
    adj = [[] for _ in range(n + 1)]
    for c, a, b, eid in sorted(edges):
        ra = leader(a)
        rb = leader(b)
        if ra != rb:
            if weight[ra] < weight[rb]:
                ra, rb = rb, ra
            comp[rb] = ra
            weight[ra] += weight[rb]
            mst[eid] = True
            adj[a].append((b, c, eid))
            adj[b].append((a, c, eid))

    height = [0] * (n + 1)
    direct = [0] * (n + 1)
    from_edge = [-1] * (n + 1)
    order = [1]
    direct[1] = 0
    for node in order:
        for to, c, eid in adj[node]:
            if to != direct[node]:
                direct[to] = node
                height[to] = height[node] + 1
                from_edge[to] = eid
                order.append(to)

    table_len = n.bit_length() + 1
    kth = [direct[:]]
    biggest = [[0] * (n + 1)]
    for v in range(1, n + 1):
        par = direct[v]
        if par:
            for to, c, eid in adj[v]:
                if to == par:
                    biggest[0][v] = c
                    break

    for _ in range(1, table_len):
        old_parent = kth[-1]
        old_max = biggest[-1]
        new_parent = [0] * (n + 1)
        new_max = [0] * (n + 1)
        for v in range(1, n + 1):
            mid = old_parent[v]
            new_parent[v] = old_parent[mid]
            new_max[v] = max(old_max[v], old_max[mid])
        kth.append(new_parent)
        biggest.append(new_max)

    def query(a, b):
        ret = 0
        if height[a] < height[b]:
            a, b = b, a
        gap = height[a] - height[b]
        for bit in range(table_len):
            if gap & (1 << bit):
                ret = max(ret, biggest[bit][a])
                a = kth[bit][a]
        if a == b:
            return ret
        for bit in range(table_len - 1, -1, -1):
            if kth[bit][a] != kth[bit][b]:
                ret = max(ret, biggest[bit][a], biggest[bit][b])
                a = kth[bit][a]
                b = kth[bit][b]
        return max(ret, biggest[0][a], biggest[0][b])

    ans = [-1] * m
    for c, a, b, eid in edges:
        if not mst[eid]:
            ans[eid] = query(a, b) - 1

    skip = list(range(n + 1))

    def alive(x):
        r = x
        while skip[r] != r:
            r = skip[r]
        while skip[x] != x:
            y = skip[x]
            skip[x] = r
            x = y
        return r

    for c, a, b, eid in sorted(edges):
        if mst[eid]:
            continue
        a = alive(a)
        b = alive(b)
        while a != b:
            if height[a] < height[b]:
                a, b = b, a
            ans[from_edge[a]] = c - 1
            skip[a] = alive(direct[a])
            a = alive(a)

# CLAUSE: finish_program
    sys.stdout.write(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    main()
