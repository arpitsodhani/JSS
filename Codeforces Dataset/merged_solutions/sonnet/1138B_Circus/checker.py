"""1138B accepts any split with matching clown and acrobat counts."""


def check_for(stdin, expected):
    data = stdin.split()
    n = int(data[0])
    clowns = data[1]
    acrobats = data[2]
    possible = expected.strip() != "-1"

    def check(out):
        row = out.split()
        if not possible:
            assert row[0] == "-1", "printed a split where none exists"
            return
        assert row[0] != "-1", "a split exists but -1 was printed"
        first = [int(v) for v in row]
        assert len(first) == n // 2, f"expected {n // 2} artists, got {len(first)}"
        assert len(set(first)) == len(first), "an artist is listed twice"
        assert all(1 <= v <= n for v in first), "index out of range"
        chosen = set(first)
        left = sum(1 for v in first if clowns[v - 1] == "1")
        right = sum(1 for v in range(1, n + 1) if v not in chosen and acrobats[v - 1] == "1")
        assert left == right, f"{left} clowns against {right} acrobats"

    return check
