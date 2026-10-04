"""1672F1 accepts any permutation of a whose sadness is the largest possible.

Sadness is n minus the largest number of cycles: fixed positions each form a
cycle, and the mismatched positions form a multigraph on values whose best
cycle decomposition has (edges - vertices + components) cycles.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n

    def sadness(a, b):
        n = len(a)
        fixed = 0
        nodes = set()
        edges = []
        for i in range(n):
            if a[i] == b[i]:
                fixed += 1
            else:
                edges.append((a[i], b[i]))
                nodes.add(a[i])
                nodes.add(b[i])
        parent = {v: v for v in nodes}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
        groups = len({find(v) for v in nodes})
        cycles = fixed + (len(edges) - len(nodes) + groups if edges else 0)
        return n - cycles

    reference = [line.split() for line in expected.split("\n") if line.strip()]

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            a = cases[case]
            b = [int(v) for v in rows[case]]
            assert sorted(b) == sorted(a), f"case {case + 1}: not a permutation of a"
            best = sadness(a, [int(v) for v in reference[case]])
            here = sadness(a, b)
            assert here >= best, f"case {case + 1}: sadness {here}, best is {best}"

    return check
