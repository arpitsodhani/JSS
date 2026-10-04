"""1009D accepts any connected coprime graph with n vertices and m edges.

The checker counts the coprime pairs itself to decide whether a graph exists,
then validates connectivity, the edge count and the gcd condition.
"""
from math import gcd


def check_for(stdin, expected):
    n, m = (int(v) for v in stdin.split()[:2])
    available = 0
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if gcd(u, v) == 1:
                available += 1
                if available > m:
                    break
        if available > m:
            break
    possible = n - 1 <= m <= available or (m >= n - 1 and available >= m)

    def check(out):
        lines = out.split()
        if not possible:
            assert lines[0].lower().startswith("impossible"), (
                f"a graph exists, printed {lines[0]!r}")
            return
        assert lines[0].lower().startswith("possible"), (
            f"expected Possible, got {lines[0]!r}")
        values = [int(v) for v in lines[1:]]
        assert len(values) == 2 * m, f"expected {m} edges, got {len(values) / 2}"
        seen = set()
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(m):
            u, v = values[2 * i], values[2 * i + 1]
            assert 1 <= u <= n and 1 <= v <= n and u != v, f"bad edge ({u}, {v})"
            key = (min(u, v), max(u, v))
            assert key not in seen, f"edge ({u}, {v}) repeated"
            seen.add(key)
            assert gcd(u, v) == 1, f"gcd({u}, {v}) is not 1"
            parent[find(u)] = find(v)
        roots = {find(v) for v in range(1, n + 1)}
        assert len(roots) == 1, "the graph is not connected"

    return check
