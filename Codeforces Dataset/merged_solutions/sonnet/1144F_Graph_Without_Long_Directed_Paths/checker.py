"""1144F accepts any orientation in which no vertex has both an incoming and an
outgoing edge; such an orientation exists exactly when the graph is bipartite.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, m = data[0], data[1]
    edges = [(data[2 + 2 * i], data[3 + 2 * i]) for i in range(m)]
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    colour = [-1] * (n + 1)
    bipartite = True
    for start in range(1, n + 1):
        if colour[start] >= 0:
            continue
        colour[start] = 0
        stack = [start]
        while stack:
            node = stack.pop()
            for nxt in adj[node]:
                if colour[nxt] < 0:
                    colour[nxt] = colour[node] ^ 1
                    stack.append(nxt)
                elif colour[nxt] == colour[node]:
                    bipartite = False

    def check(out):
        lines = out.split()
        if not bipartite:
            assert lines[0].upper() == "NO", f"graph is not bipartite, got {lines[0]!r}"
            return
        assert lines[0].upper() == "YES", f"an orientation exists, got {lines[0]!r}"
        word = lines[1]
        assert len(word) == m, f"expected {m} characters, got {len(word)}"
        assert set(word) <= {"0", "1"}, f"bad characters in {word!r}"
        outgoing = [False] * (n + 1)
        incoming = [False] * (n + 1)
        for (u, v), ch in zip(edges, word):
            if ch == "0":
                outgoing[u] = True
                incoming[v] = True
            else:
                outgoing[v] = True
                incoming[u] = True
        for v in range(1, n + 1):
            assert not (outgoing[v] and incoming[v]), f"vertex {v} has a path of length two"

    return check
