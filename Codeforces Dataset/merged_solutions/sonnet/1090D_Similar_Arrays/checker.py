"""1090D accepts any pair of arrays giving the same comparison results."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    m = data[1]
    pairs = [(data[2 + 2 * i], data[3 + 2 * i]) for i in range(m)]
    possible = expected.strip().split("\n")[0].strip().upper() == "YES"

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows[0].upper() == "NO", "printed arrays where none exist"
            return
        assert rows[0].upper() == "YES", "arrays exist but NO was printed"
        first = [int(v) for v in rows[1].split()]
        second = [int(v) for v in rows[2].split()]
        assert len(first) == n and len(second) == n, "wrong array lengths"
        assert all(1 <= v <= n for v in first + second), "a value is outside 1..n"
        assert len(set(first)) == n, "the first array must have distinct values"
        assert len(set(second)) < n, "the second array must repeat a value"
        for a, b in pairs:
            left = (first[a - 1] > first[b - 1]) - (first[a - 1] < first[b - 1])
            right = (second[a - 1] > second[b - 1]) - (second[a - 1] < second[b - 1])
            assert left == right, f"comparison ({a},{b}) differs"

    return check
