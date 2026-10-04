"""989B accepts any filled-in string for which p is not a period."""


def check_for(stdin, expected):
    data = stdin.split()
    n = int(data[0])
    p = int(data[1])
    s = data[2]
    possible = expected.strip().lower() != "no"

    def check(out):
        row = out.strip()
        if not possible:
            assert row.lower() == "no", "printed a string where none exists"
            return
        assert row.lower() != "no", "a string exists but No was printed"
        assert len(row) == n, f"expected {n} characters, got {len(row)}"
        assert set(row) <= set("01"), "only 0 and 1 are allowed"
        for i in range(n):
            if s[i] != ".":
                assert row[i] == s[i], f"character {i + 1} was fixed to {s[i]}"
        assert any(row[i] != row[i + p] for i in range(n - p)), "p is still a period"

    return check
