"""440D accepts any minimum set of roads whose removal leaves a state of exactly
k towns.

The checker recomputes the minimum by brute force over connected subsets (the
samples are tiny) and then verifies the printed roads really produce such a
state.
"""
from itertools import combinations


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, k = data[0], data[1]
    edges = [(data[2 + 2 * i], data[3 + 2 * i]) for i in range(n - 1)]
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    best = None
    for combo in combinations(range(1, n + 1), k):
        group = set(combo)
        stack = [combo[0]]
        seen = {combo[0]}
        while stack:
            node = stack.pop()
            for nxt in adj[node]:
                if nxt in group and nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        if len(seen) != k:
            continue
        cuts = sum(1 for u, v in edges if (u in group) != (v in group))
        if best is None or cuts < best:
            best = cuts

    def check(out):
        tokens = out.split()
        count = int(tokens[0])
        chosen = [int(v) for v in tokens[1:1 + count]]
        assert count == best, f"printed {count} roads, the minimum is {best}"
        assert len(chosen) == count, f"expected {count} indices, got {len(chosen)}"
        assert len(set(chosen)) == count, "repeated road index"
        assert all(1 <= i <= n - 1 for i in chosen), "road index out of range"
        cut = set(chosen)
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for index, (u, v) in enumerate(edges, start=1):
            if index in cut:
                continue
            parent[find(u)] = find(v)
        sizes = {}
        for v in range(1, n + 1):
            root = find(v)
            sizes[root] = sizes.get(root, 0) + 1
        assert k in sizes.values(), f"no state has exactly {k} towns"

    return check
