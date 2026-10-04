"""639B accepts any tree with the recorded diameter and rooted height.

A tree exists exactly when d <= 2h, and, when d == h, the extra vertices need a
vertex at depth 1 to hang from, which needs h >= 2 whenever n > d + 1.
"""
from collections import deque


def check_for(stdin, expected):
    n, d, h = (int(v) for v in stdin.split())
    possible = d <= 2 * h and not (d == h == 1 and n > 2)

    def check(out):
        got = out.split()
        if len(got) == 1 and got[0] == "-1":
            assert not possible, "printed -1 but a tree exists"
            return
        assert possible, "printed a tree but none exists"
        pairs = [(int(got[2 * i]), int(got[2 * i + 1])) for i in range(n - 1)]
        adj = {v: [] for v in range(1, n + 1)}
        for u, v in pairs:
            assert 1 <= u <= n and 1 <= v <= n and u != v, f"bad edge ({u}, {v})"
            adj[u].append(v)
            adj[v].append(u)

        def far(root):
            dist = {root: 0}
            queue = deque([root])
            while queue:
                node = queue.popleft()
                for nxt in adj[node]:
                    if nxt not in dist:
                        dist[nxt] = dist[node] + 1
                        queue.append(nxt)
            return dist

        base = far(1)
        assert len(base) == n, "the graph is not connected"
        assert max(base.values()) == h, f"height is {max(base.values())}, expected {h}"
        best = 0
        for v in range(1, n + 1):
            best = max(best, max(far(v).values()))
        assert best == d, f"diameter is {best}, expected {d}"

    return check
