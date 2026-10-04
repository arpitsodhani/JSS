"""412C accepts any pattern with the fewest '?' that matches all the inputs.

A position needs '?' exactly when two inputs pin it to different letters;
otherwise any single letter works, so only the count of '?' is fixed.
"""


def check_for(stdin, expected):
    rows = stdin.split()[1:]
    width = len(rows[0])
    forced = []
    for j in range(width):
        letters = {row[j] for row in rows if row[j] != "?"}
        forced.append(letters)
    wanted = sum(1 for letters in forced if len(letters) > 1)

    def check(out):
        got = out.split()[0]
        assert len(got) == width, f"length {len(got)}, expected {width}"
        assert got.count("?") == wanted, (
            f"used {got.count('?')} question marks, the minimum is {wanted}")
        for j in range(width):
            if len(forced[j]) > 1:
                assert got[j] == "?", f"position {j + 1} must be '?'"
            elif len(forced[j]) == 1:
                assert got[j] == next(iter(forced[j])), f"position {j + 1} is pinned"
            else:
                assert got[j].isalpha() and got[j].islower(), f"position {j + 1} must be a letter"

    return check
