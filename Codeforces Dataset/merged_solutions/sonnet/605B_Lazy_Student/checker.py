"""605B accepts any graph consistent with the recorded MST, so check the rules.

The b=1 edges must form a spanning tree, the graph must be simple, and every
b=0 edge must be at least as heavy as the heaviest edge on the tree path between
its ends - that is exactly the cycle property that makes the marked tree an MST.
Feasibility for the -1 case is decided by the same star construction the
solutions use: tree edges hang off vertex 1, and a non-tree edge of weight w
needs two vertices already attached by edges no heavier than w.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    n, m = int(tokens[0]), int(tokens[1])
    edges = [(int(tokens[2 + 2 * i]), int(tokens[3 + 2 * i])) for i in range(m)]

    order = sorted(range(m), key=lambda i: (edges[i][0], -edges[i][1]))
    attached, x, y = 1, 2, 3
    feasible = True
    for i in order:
        if edges[i][1] == 1:
            attached += 1
        else:
            if x >= y or y > attached:
                feasible = False
                break
            y += 1
            if y > attached:
                x += 1
                y = x + 1
    if n == 1:
        feasible = m == 0

    def check(out):
        got = out.split()
        if len(got) == 1 and got[0] == "-1":
            assert not feasible, "printed -1 but a graph exists"
            return
        assert feasible, "printed a graph but none exists"
        assert len(got) == 2 * m, f"expected {2 * m} numbers, got {len(got)}"
        ends = [(int(got[2 * i]), int(got[2 * i + 1])) for i in range(m)]
        seen = set()
        for u, v in ends:
            assert 1 <= u <= n and 1 <= v <= n, f"vertex out of range in ({u}, {v})"
            assert u != v, f"self loop at {u}"
            key = (min(u, v), max(u, v))
            assert key not in seen, f"duplicate edge {key}"
            seen.add(key)
        tree = [(ends[i], edges[i][0]) for i in range(m) if edges[i][1] == 1]
        assert len(tree) == n - 1, "the marked edges are not a spanning tree"
        adj = {v: [] for v in range(1, n + 1)}
        for (u, v), w in tree:
            adj[u].append((v, w))
            adj[v].append((u, w))
        # heaviest edge on the tree path from every vertex, by BFS from each root
        far = {}
        for root in range(1, n + 1):
            seen_v = {root: 0}
            stack = [root]
            while stack:
                node = stack.pop()
                for nxt, w in adj[node]:
                    if nxt not in seen_v:
                        seen_v[nxt] = max(seen_v[node], w)
                        stack.append(nxt)
            assert len(seen_v) == n, "the marked edges do not span every vertex"
            far[root] = seen_v
        for i in range(m):
            if edges[i][1] == 0:
                u, v = ends[i]
                assert edges[i][0] >= far[u][v], (
                    f"edge {i + 1} of weight {edges[i][0]} is lighter than the "
                    f"tree path maximum {far[u][v]}, so the tree is not an MST")

    return check
