"""330B accepts any minimum-size road set, so compare against the rules, not the
sample output.

A connected graph on n vertices needs at least n-1 edges, and a tree of diameter
at most 2 is exactly a star. So every optimal answer is a star of n-1 edges whose
centre appears in no forbidden pair.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    n = int(tokens[0])
    m = int(tokens[1])
    banned = set()
    for i in range(m):
        a = int(tokens[2 + 2 * i])
        b = int(tokens[3 + 2 * i])
        banned.add((a, b))
        banned.add((b, a))

    def check(out):
        got = out.split()
        assert got, "empty output"
        count = int(got[0])
        assert count == n - 1, f"used {count} roads, minimum is {n - 1}"
        assert len(got) == 1 + 2 * count, f"expected {count} road lines, got {len(got) - 1} numbers"
        edges = [(int(got[1 + 2 * i]), int(got[2 + 2 * i])) for i in range(count)]
        for a, b in edges:
            assert 1 <= a <= n and 1 <= b <= n, f"road ({a}, {b}) out of range"
            assert a != b, f"road ({a}, {b}) is a self loop"
            assert (a, b) not in banned, f"road ({a}, {b}) is forbidden"
        if count == 0:
            return
        centre_options = set(edges[0])
        for a, b in edges[1:]:
            centre_options &= {a, b}
        assert centre_options, "roads do not all share one centre, so the graph is not a star"
        centre = centre_options.pop()
        leaves = {b if a == centre else a for a, b in edges}
        assert len(leaves) == count, "a leaf is repeated, so the graph is not connected"
        assert leaves == set(range(1, n + 1)) - {centre}, "some city is left unconnected"

    return check
