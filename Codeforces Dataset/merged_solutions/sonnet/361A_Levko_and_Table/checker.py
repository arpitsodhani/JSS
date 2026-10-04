"""361A accepts any table whose every row and column sums to k, with entries
bounded by 1000 in absolute value."""


def check_for(stdin, expected):
    n, k = (int(v) for v in stdin.split())

    def check(out):
        got = [int(v) for v in out.split()]
        assert len(got) == n * n, f"expected {n * n} numbers, got {len(got)}"
        table = [got[r * n:(r + 1) * n] for r in range(n)]
        for value in got:
            assert abs(value) <= 1000, f"entry {value} exceeds 1000 in absolute value"
        for r in range(n):
            assert sum(table[r]) == k, f"row {r + 1} sums to {sum(table[r])}, not {k}"
        for c in range(n):
            column = sum(table[r][c] for r in range(n))
            assert column == k, f"column {c + 1} sums to {column}, not {k}"

    return check
