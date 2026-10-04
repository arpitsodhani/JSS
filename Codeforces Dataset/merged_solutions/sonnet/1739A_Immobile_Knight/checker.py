"""1739A accepts any isolated cell, or any cell when none is isolated."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    cases = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(t)]
    steps = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

    def isolated(n, m, row, column):
        for dr, dc in steps:
            if 1 <= row + dr <= n and 1 <= column + dc <= m:
                return False
        return True

    def check(out):
        rows = [line for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            n, m = cases[case]
            row, column = (int(v) for v in rows[case].split())
            assert 1 <= row <= n and 1 <= column <= m, f"case {case + 1}: cell off the board"
            any_isolated = any(
                isolated(n, m, r, c) for r in range(1, n + 1) for c in range(1, m + 1)
            )
            if any_isolated:
                assert isolated(n, m, row, column), f"case {case + 1}: cell is not isolated"

    return check
