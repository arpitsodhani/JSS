"""858F accepts any set of episodes using each road at most once, of maximum
size.

Each episode consumes two adjacent roads, so the maximum is the sum over
connected components of floor(edges / 2), which the checker recomputes.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, m = data[0], data[1]
    edges = [(data[2 + 2 * i], data[3 + 2 * i]) for i in range(m)]
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        parent[find(u)] = find(v)
    per_component = {}
    for u, v in edges:
        root = find(u)
        per_component[root] = per_component.get(root, 0) + 1
    best = sum(count // 2 for count in per_component.values())
    lookup = {}
    for u, v in edges:
        lookup[(min(u, v), max(u, v))] = True

    def check(out):
        tokens = out.split()
        count = int(tokens[0])
        assert count == best, f"printed {count} episodes, the maximum is {best}"
        assert len(tokens) == 1 + 3 * count, "wrong number of episode fields"
        seen = set()
        for i in range(count):
            x = int(tokens[1 + 3 * i])
            y = int(tokens[2 + 3 * i])
            z = int(tokens[3 + 3 * i])
            for a, b in ((x, y), (y, z)):
                key = (min(a, b), max(a, b))
                assert key in lookup, f"({a}, {b}) is not a road"
                assert key not in seen, f"road ({a}, {b}) used twice"
                seen.add(key)

    return check
