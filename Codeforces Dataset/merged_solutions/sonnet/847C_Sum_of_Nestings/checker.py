"""847C accepts any regular bracket sequence with the requested total nesting."""


def check_for(stdin, expected):
    n, k = (int(v) for v in stdin.split())
    possible = expected.strip() != "Impossible"

    def check(out):
        row = out.strip()
        if not possible:
            assert row == "Impossible", "printed a sequence where none exists"
            return
        assert row != "Impossible", "a sequence exists but Impossible was printed"
        assert len(row) == 2 * n, f"expected {2 * n} characters, got {len(row)}"
        depth = 0
        total = 0
        for ch in row:
            if ch == "(":
                total += depth
                depth += 1
            else:
                depth -= 1
                assert depth >= 0, "the sequence is not regular"
        assert depth == 0, "the sequence is not regular"
        assert total == k, f"nesting sums to {total}, expected {k}"

    return check
