"""550D accepts any connected k-regular graph that contains a bridge."""


def check_for(stdin, expected):
    k = int(stdin.split()[0])
    possible = expected.strip().split("\n")[0].strip().upper() == "YES"

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows[0].upper() == "NO", "printed a graph where none exists"
            return
        assert rows[0].upper() == "YES", "a graph exists but NO was printed"
        n, m = (int(v) for v in rows[1].split())
        assert 1 <= n <= 10 ** 6 and m <= 10 ** 6, "graph too large"
        edges = []
        degree = [0] * (n + 1)
        seen = set()
        for i in range(m):
            u, v = (int(x) for x in rows[2 + i].split())
            assert 1 <= u <= n and 1 <= v <= n and u != v, "bad edge"
            key = (min(u, v), max(u, v))
            assert key not in seen, "repeated edge"
            seen.add(key)
            edges.append((u, v))
            degree[u] += 1
            degree[v] += 1
        for v in range(1, n + 1):
            assert degree[v] == k, f"vertex {v} has degree {degree[v]}, expected {k}"

        def pieces(skip):
            adj = [[] for _ in range(n + 1)]
            for i, (u, v) in enumerate(edges):
                if i == skip:
                    continue
                adj[u].append(v)
                adj[v].append(u)
            found = [False] * (n + 1)
            found[1] = True
            stack = [1]
            count = 1
            while stack:
                x = stack.pop()
                for y in adj[x]:
                    if not found[y]:
                        found[y] = True
                        count += 1
                        stack.append(y)
            return count

        assert pieces(-1) == n, "the graph is not connected"
        assert any(pieces(i) < n for i in range(m)), "the graph has no bridge"

    return check
