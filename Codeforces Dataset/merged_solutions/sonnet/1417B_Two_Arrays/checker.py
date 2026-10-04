"""1417B accepts any colouring with the smallest total misfortune.

The printed colouring is scored by counting pairs summing to T inside each
colour, and compared with the reference colouring's score.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        target = data[pos + 1]
        pos += 2
        cases.append((target, data[pos:pos + n]))
        pos += n
    reference = [line.split() for line in expected.split("\n") if line.strip()]

    def score(target, a, colours):
        total = 0
        for side in (0, 1):
            tally = {}
            for i in range(len(a)):
                if colours[i] != side:
                    continue
                total += tally.get(target - a[i], 0)
                tally[a[i]] = tally.get(a[i], 0) + 1
        return total

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            target, a = cases[case]
            colours = [int(v) for v in rows[case]]
            assert len(colours) == len(a), f"case {case + 1}: expected {len(a)} colours"
            assert set(colours) <= {0, 1}, f"case {case + 1}: colours must be 0 or 1"
            best = score(target, a, [int(v) for v in reference[case]])
            here = score(target, a, colours)
            assert here <= best, f"case {case + 1}: misfortune {here}, best is {best}"

    return check
