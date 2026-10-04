"""370C accepts any distribution with the most distinct-coloured pairs.

Both mitten multisets have to match the input, and the number of children whose
two mittens differ has to match the reference answer.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    colours = sorted(data[2:2 + n])
    best = int(expected.split("\n")[0])

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        count = int(rows[0][0])
        assert count == best, f"claimed {count} happy children, the most is {best}"
        lefts = []
        rights = []
        happy = 0
        for row in rows[1:1 + n]:
            left, right = (int(v) for v in row)
            lefts.append(left)
            rights.append(right)
            if left != right:
                happy += 1
        assert len(lefts) == n, f"expected {n} children, got {len(lefts)}"
        assert sorted(lefts) == colours, "the left mittens changed"
        assert sorted(rights) == colours, "the right mittens changed"
        assert happy == count, f"printed {count} but {happy} children have distinct mittens"

    return check
