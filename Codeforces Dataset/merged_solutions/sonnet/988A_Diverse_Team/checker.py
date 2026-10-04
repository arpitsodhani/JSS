"""988A accepts any team of k students with distinct ratings."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    k = data[1]
    ratings = data[2:2 + n]
    possible = expected.strip().split("\n")[0].strip().upper() == "YES"

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows[0].upper() == "NO", "printed a team where none exists"
            return
        assert rows[0].upper() == "YES", "a team exists but NO was printed"
        picked = [int(v) for v in rows[1].split()]
        assert len(picked) == k, f"expected {k} students, got {len(picked)}"
        assert len(set(picked)) == k, "a student is listed twice"
        assert all(1 <= v <= n for v in picked), "index out of range"
        values = [ratings[v - 1] for v in picked]
        assert len(set(values)) == k, "two team members share a rating"

    return check
