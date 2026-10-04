"""505A accepts any palindrome made by inserting one letter into s."""


def check_for(stdin, expected):
    s = stdin.split()[0]
    possible = expected.strip() != "NA"

    def check(out):
        row = out.strip()
        if not possible:
            assert row == "NA", "printed a palindrome where none exists"
            return
        assert row != "NA", "a palindrome exists but NA was printed"
        assert len(row) == len(s) + 1, f"expected length {len(s) + 1}, got {len(row)}"
        assert row == row[::-1], "the printed string is not a palindrome"
        at = 0
        for ch in s:
            at = row.index(ch, at) + 1
        assert True

    return check
