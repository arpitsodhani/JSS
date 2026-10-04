"""883G accepts any orientations that hit the best and worst reachable counts.

Both printed plans are replayed: the graph is oriented as printed and the set
reachable from s is recomputed, then compared with the two optimal counts.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, m, s = data[0], data[1], data[2]
    edges = [(data[3 + 3 * i], data[4 + 3 * i], data[5 + 3 * i]) for i in range(m)]
    loose = sum(1 for kind, u, v in edges if kind == 2)

    def reach(directions):
        adj = [[] for _ in range(n + 1)]
        at = 0
        for kind, u, v in edges:
            if kind == 1:
                adj[u].append(v)
                continue
            if directions[at] == "+":
                adj[u].append(v)
            else:
                adj[v].append(u)
            at += 1
        seen = [False] * (n + 1)
        seen[s] = True
        stack = [s]
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if not seen[u]:
                    seen[u] = True
                    stack.append(u)
        return sum(seen)

    wanted = [int(line) for line in expected.split("\n") if line.strip() and line.strip().lstrip("-").isdigit()]

    def check(out):
        rows = out.split("\n")
        rows = [row.strip() for row in rows]
        numbers = []
        plans = []
        for row in rows:
            if row.isdigit():
                numbers.append(int(row))
            elif set(row) <= {"+", "-"} and row != "":
                plans.append(row)
        if loose == 0:
            plans = ["", ""]
        assert len(numbers) >= 2, "expected two counts"
        assert len(plans) >= 2, "expected two orientation strings"
        for i in (0, 1):
            assert len(plans[i]) == loose, f"plan {i + 1} orients {len(plans[i])} edges, expected {loose}"
            assert reach(plans[i]) == numbers[i], f"plan {i + 1} reaches {reach(plans[i])}, printed {numbers[i]}"
        assert numbers[0] == wanted[0], f"maximum {numbers[0]}, best is {wanted[0]}"
        assert numbers[1] == wanted[1], f"minimum {numbers[1]}, best is {wanted[1]}"

    return check
