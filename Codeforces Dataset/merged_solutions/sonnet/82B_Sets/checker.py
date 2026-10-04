"""82B accepts the sets in any order, so the printed sets are checked directly.

They must be disjoint, non-empty, and the unions of every pair must be exactly
the pieces of paper from the input.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    pos = 1
    papers = []
    for _ in range(n * (n - 1) // 2):
        k = data[pos]
        pos += 1
        papers.append(tuple(sorted(data[pos:pos + k])))
        pos += k
    papers.sort()

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        assert len(rows) == n, f"expected {n} sets, got {len(rows)}"
        sets = []
        for row in rows:
            values = [int(v) for v in row]
            assert values[0] == len(values) - 1, f"set says {values[0]} elements, lists {len(values) - 1}"
            assert values[0] >= 1, "a set is empty"
            sets.append(set(values[1:]))
        seen = set()
        for group in sets:
            assert not (seen & group), "the sets overlap"
            seen |= group
        built = []
        for i in range(n):
            for j in range(i + 1, n):
                built.append(tuple(sorted(sets[i] | sets[j])))
        built.sort()
        assert built == papers, "the pairwise unions differ from the pieces of paper"

    return check
