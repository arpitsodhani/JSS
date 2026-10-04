"""1368E accepts any set of closures within the 4n/7 budget.

The check closes the printed spots and then looks for any spot that still has
both an entering and a leaving track, which is exactly a dangerous path.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        tracks = []
        for _ in range(m):
            tracks.append((data[pos], data[pos + 1]))
            pos += 2
        cases.append((n, tracks))

    def check(out):
        rows = [line.strip() for line in out.split("\n")]
        rows = [line for line in rows if line != ""] if False else rows
        at = 0
        for n, tracks in cases:
            while rows[at].strip() == "" and rows[at] != "0":
                at += 1
            k = int(rows[at])
            at += 1
            shut = [int(v) for v in rows[at].split()] if k else []
            at += 1
            assert len(shut) == k, f"said {k} spots, listed {len(shut)}"
            assert len(set(shut)) == k, "a spot is listed twice"
            assert all(1 <= v <= n for v in shut), "spot out of range"
            assert 7 * k <= 4 * n, f"closed {k} spots, the budget is 4*{n}/7"
            gone = set(shut)
            enters = [False] * (n + 1)
            leaves = [False] * (n + 1)
            for x, y in tracks:
                if x in gone or y in gone:
                    continue
                leaves[x] = True
                enters[y] = True
            for v in range(1, n + 1):
                assert not (enters[v] and leaves[v]), f"spot {v} still has a dangerous path"

    return check
