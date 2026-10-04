"""1278E accepts any valid family of segments, so the printed one is checked.

Every endpoint from 1 to 2n has to appear once, and two segments must overlap
without nesting exactly when the corresponding vertices share a tree edge.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    edges = set()
    for i in range(n - 1):
        x = data[1 + 2 * i]
        y = data[2 + 2 * i]
        edges.add((min(x, y), max(x, y)))

    def check(out):
        numbers = [int(v) for v in out.split()]
        assert len(numbers) == 2 * n, f"expected {2 * n} numbers, got {len(numbers)}"
        spans = [(numbers[2 * i], numbers[2 * i + 1]) for i in range(n)]
        seen = []
        for l, r in spans:
            assert 1 <= l < r <= 2 * n, f"segment ({l}, {r}) is not valid"
            seen.append(l)
            seen.append(r)
        assert sorted(seen) == list(range(1, 2 * n + 1)), "the endpoints are not a permutation of 1..2n"
        for i in range(n):
            for j in range(i + 1, n):
                a, b = spans[i]
                c, d = spans[j]
                crossing = (a < c < b < d) or (c < a < d < b)
                linked = (i + 1, j + 1) in edges
                assert crossing == linked, \
                    f"segments {i + 1} and {j + 1}: crossing={crossing}, edge={linked}"

    return check
