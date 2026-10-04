"""727E accepts any valid list of games, printed from any starting position.

The names are written clockwise on a circle, so a printed list is correct when
its names concatenate to some rotation of the string on the CD and no game is
used twice.
"""


def check_for(stdin, expected):
    lines = stdin.split("\n")
    n, k = (int(v) for v in lines[0].split())
    disc = lines[1].strip()
    g = int(lines[2])
    names = [lines[3 + i].strip() for i in range(g)]
    possible = expected.strip().split("\n")[0].strip().upper() == "YES"

    def check(out):
        parts = out.split()
        if not possible:
            assert parts and parts[0].upper() == "NO", "a list was printed for an impossible disc"
            return
        assert parts[0].upper() == "YES", "a valid list exists but NO was printed"
        picked = [int(v) for v in parts[1:]]
        assert len(picked) == n, f"expected {n} games, got {len(picked)}"
        assert len(set(picked)) == n, "a game was burned twice"
        assert all(1 <= v <= g for v in picked), "game number out of range"
        written = "".join(names[v - 1] for v in picked)
        assert len(written) == len(disc) and written in disc + disc, \
            "the names do not spell the string on the CD"

    return check
