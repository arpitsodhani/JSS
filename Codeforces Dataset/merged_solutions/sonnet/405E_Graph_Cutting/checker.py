"""405E accepts any partition of the edges into adjacent pairs.

A connected graph can be cut exactly when it has an even number of edges, so the
checker recomputes that and then verifies every printed triple uses two real
edges sharing the middle vertex, with each edge consumed exactly once.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, m = data[0], data[1]
    edges = {}
    for i in range(m):
        a, b = data[2 + 2 * i], data[3 + 2 * i]
        edges[(min(a, b), max(a, b))] = i

    def check(out):
        text = out.strip()
        if m % 2:
            assert text.lower().startswith("no solution"), (
                f"m is odd, expected 'No solution', got {text[:20]!r}")
            return
        assert not text.lower().startswith("no"), "a cutting exists"
        tokens = [int(v) for v in text.split()]
        assert len(tokens) == 3 * (m // 2), (
            f"expected {m // 2} triples, got {len(tokens) / 3}")
        left = set(edges)
        for i in range(0, len(tokens), 3):
            x, y, z = tokens[i], tokens[i + 1], tokens[i + 2]
            for a, b in ((x, y), (y, z)):
                key = (min(a, b), max(a, b))
                assert key in edges, f"({a}, {b}) is not an edge"
                assert key in left, f"edge ({a}, {b}) used twice"
                left.discard(key)
        assert not left, f"{len(left)} edges were never used"

    return check
