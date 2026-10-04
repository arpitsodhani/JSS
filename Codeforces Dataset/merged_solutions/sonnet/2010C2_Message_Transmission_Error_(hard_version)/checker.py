"""2010C2 accepts any message whose doubled copy merges into t."""


def check_for(stdin, expected):
    t = stdin.split()[0]
    possible = expected.strip().split("\n")[0].strip().upper() == "YES"

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows[0].upper() == "NO", "printed a message where none exists"
            return
        assert rows[0].upper() == "YES", "a message exists but NO was printed"
        s = rows[1]
        n = len(t)
        size = len(s)
        overlap = 2 * size - n
        assert 0 < overlap < size, f"overlap {overlap} is not allowed"
        assert t[:size] == s and t[n - size:] == s, "the message does not rebuild t"

    return check
