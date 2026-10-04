"""1385E accepts any acyclic orientation that keeps the pre-directed edges.

The checker recomputes whether the directed part is acyclic, then verifies the
printed orientation keeps those edges and has no directed cycle.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        edges = []
        for _ in range(m):
            edges.append((data[pos], data[pos + 1], data[pos + 2]))
            pos += 3
        cases.append((n, m, edges))

    def acyclic(n, arcs):
        adj = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)
        for x, y in arcs:
            adj[x].append(y)
            indeg[y] += 1
        queue = [v for v in range(1, n + 1) if indeg[v] == 0]
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            for nxt in adj[node]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    queue.append(nxt)
        return len(queue) == n

    def check(out):
        tokens = out.split()
        at = 0
        for n, m, edges in cases:
            possible = acyclic(n, [(x, y) for kind, x, y in edges if kind == 1])
            verdict = tokens[at].upper()
            at += 1
            if not possible:
                assert verdict == "NO", f"expected NO, got {verdict}"
                continue
            assert verdict == "YES", f"expected YES, got {verdict}"
            arcs = []
            for kind, x, y in edges:
                u = int(tokens[at])
                v = int(tokens[at + 1])
                at += 2
                assert {u, v} == {x, y}, f"edge ({x}, {y}) became ({u}, {v})"
                if kind == 1:
                    assert (u, v) == (x, y), f"directed edge ({x}, {y}) was flipped"
                arcs.append((u, v))
            assert acyclic(n, arcs), "the orientation has a cycle"
        assert at == len(tokens), "extra output"

    return check
