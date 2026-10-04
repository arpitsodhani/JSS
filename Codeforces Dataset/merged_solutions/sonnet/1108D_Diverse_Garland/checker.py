"""1108D accepts any minimum recolouring, so check the count and the garland."""


def check_for(stdin, expected):
    tokens = stdin.split()
    n = int(tokens[0])
    s = tokens[1]
    best = 0
    prev = ""
    i = 0
    colours = "RGB"
    work = list(s)
    while i < n:
        if i and work[i] == work[i - 1]:
            best += 1
            for c in colours:
                if c != work[i - 1] and (i + 1 >= n or c != work[i + 1]):
                    work[i] = c
                    break
        i += 1

    def check(out):
        got = out.split()
        assert len(got) == 2, f"expected a count and a garland, got {got}"
        count = int(got[0])
        garland = got[1]
        assert count == best, f"used {count} recolours, the minimum is {best}"
        assert len(garland) == n, f"garland has length {len(garland)}, expected {n}"
        assert set(garland) <= set("RGB"), "garland uses a colour outside RGB"
        changed = sum(1 for a, b in zip(s, garland) if a != b)
        assert changed == count, f"garland differs in {changed} places but {count} was reported"
        for i in range(1, n):
            assert garland[i] != garland[i - 1], f"lamps {i} and {i + 1} share a colour"

    return check
