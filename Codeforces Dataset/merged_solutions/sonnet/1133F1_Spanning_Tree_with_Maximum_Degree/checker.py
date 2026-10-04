"""1133F1 accepts any spanning tree whose maximum degree is as large as possible.

Every edge of the highest-degree vertex can be kept in some spanning tree, so the
best achievable maximum degree is that vertex's degree in the whole graph.
"""


def check_for(stdin, expected):
    tokens = [int(v) for v in stdin.split()]
    n, m = tokens[0], tokens[1]
    edges = {(min(tokens[2 + 2 * i], tokens[3 + 2 * i]), max(tokens[2 + 2 * i], tokens[3 + 2 * i]))
             for i in range(m)}
    degree = [0] * (n + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    best = max(degree)

    def check(out):
        got = [int(v) for v in out.split()]
        assert len(got) == 2 * (n - 1), f"expected {n - 1} edges, got {len(got) // 2}"
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        used = [0] * (n + 1)
        for i in range(n - 1):
            u, v = got[2 * i], got[2 * i + 1]
            assert (min(u, v), max(u, v)) in edges, f"edge ({u}, {v}) is not in the graph"
            ru, rv = find(u), find(v)
            assert ru != rv, f"edge ({u}, {v}) closes a cycle"
            parent[ru] = rv
            used[u] += 1
            used[v] += 1
        assert max(used) == best, f"maximum degree {max(used)}, the best possible is {best}"

    return check
