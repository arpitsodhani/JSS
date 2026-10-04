"""847A accepts any single list built from the given ones."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    prev = [0] * (n + 1)
    nxt = [0] * (n + 1)
    for i in range(1, n + 1):
        prev[i] = data[2 * i - 1]
        nxt[i] = data[2 * i]

    def links(p, q):
        pairs = set()
        for v in range(1, n + 1):
            if q[v]:
                pairs.add((v, q[v]))
        return pairs

    wanted = links(prev, nxt)

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        assert len(rows) == n, f"expected {n} rows, got {len(rows)}"
        p = [0] * (n + 1)
        q = [0] * (n + 1)
        for i in range(1, n + 1):
            p[i] = int(rows[i - 1][0])
            q[i] = int(rows[i - 1][1])
        for v in range(1, n + 1):
            if q[v]:
                assert p[q[v]] == v, f"links at {v} are not symmetric"
            if p[v]:
                assert q[p[v]] == v, f"links at {v} are not symmetric"
        heads = [v for v in range(1, n + 1) if p[v] == 0]
        assert len(heads) == 1, f"expected one list, found {len(heads)} heads"
        walk = heads[0]
        seen = 0
        while walk:
            seen += 1
            walk = q[walk]
        assert seen == n, f"the list holds {seen} cells, expected {n}"
        assert wanted <= links(p, q), "an original link was broken"

    return check
