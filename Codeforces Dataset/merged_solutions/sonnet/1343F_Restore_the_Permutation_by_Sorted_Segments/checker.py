"""1343F accepts any permutation matching the given sorted segments.

Each segment has to be exactly the sorted contents of some window ending at a
distinct position r >= 2 of the printed permutation.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        pieces = []
        for _ in range(n - 1):
            size = data[pos]
            pos += 1
            pieces.append(sorted(data[pos:pos + size]))
            pos += size
        cases.append((n, pieces))

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            n, pieces = cases[case]
            p = [int(v) for v in rows[case]]
            assert sorted(p) == list(range(1, n + 1)), f"case {case + 1}: not a permutation"
            spot = {value: i for i, value in enumerate(p)}
            taken = set()
            for piece in pieces:
                places = [spot[value] for value in piece]
                low = min(places)
                high = max(places)
                assert high - low + 1 == len(piece), f"case {case + 1}: a segment is not contiguous"
                assert sorted(p[low:high + 1]) == piece, f"case {case + 1}: a segment does not match"
                assert high >= 1, f"case {case + 1}: a segment ends at position 1"
                assert high not in taken, f"case {case + 1}: two segments end at the same position"
                taken.add(high)

    return check
