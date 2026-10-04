"""2010C1 accepts any s whose doubled form with a positive overlap shorter than
|s| reproduces t."""


def check_for(stdin, expected):
    t = stdin.split()[0]

    def possible():
        for size in range((len(t) + 2) // 2, len(t)):
            overlap = 2 * size - len(t)
            if 1 <= overlap < size and t[:size] == t[len(t) - size:]:
                return True
        return False

    exists = possible()

    def check(out):
        got = out.split()
        if got[0].upper() == "NO":
            assert not exists, "printed NO but an s exists"
            return
        assert got[0].upper() == "YES", f"unexpected first token {got[0]}"
        assert exists, "printed YES but no s exists"
        s = got[1]
        overlap = 2 * len(s) - len(t)
        assert 1 <= overlap < len(s), f"overlap {overlap} is not in [1, {len(s) - 1}]"
        assert s + s[overlap:] == t, f"{s} does not merge into {t}"

    return check
