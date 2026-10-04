"""1876C accepts any set of operations whose circled indices spell the leftovers.

The printed p is checked by circling exactly those indices and reading the
uncircled values in index order: the two sequences have to be equal.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    a = data[1:1 + n]
    possible = expected.strip() != "-1"

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows[0] == "-1", "printed operations where none exist"
            return
        assert rows[0] != "-1", "a solution exists but -1 was printed"
        count = int(rows[0])
        picks = [int(v) for v in rows[1].split()] if count else []
        assert len(picks) == count, f"said {count} operations, listed {len(picks)}"
        assert all(1 <= v <= n for v in picks), "index out of range"
        circled = set(picks)
        left = [a[i] for i in range(n) if i + 1 not in circled]
        assert left == picks, f"leftovers {left} differ from the operations {picks}"

    return check
