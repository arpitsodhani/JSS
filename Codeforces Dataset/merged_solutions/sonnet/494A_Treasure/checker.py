"""494A accepts any assignment of ')' counts that makes the string balanced."""


def check_for(stdin, expected):
    s = stdin.strip()
    possible = expected.strip() != "-1"

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows[0] == "-1", "printed an assignment where none exists"
            return
        assert rows[0] != "-1", "an assignment exists but -1 was printed"
        counts = [int(v) for v in rows]
        assert len(counts) == s.count("#"), f"expected {s.count('#')} numbers, got {len(counts)}"
        assert all(v >= 1 for v in counts), "each '#' needs at least one ')'"
        balance = 0
        at = 0
        for ch in s:
            if ch == "(":
                balance += 1
            elif ch == ")":
                balance -= 1
            else:
                balance -= counts[at]
                at += 1
            assert balance >= 0, "a prefix has more ')' than '('"
        assert balance == 0, "the string is not balanced"

    return check
