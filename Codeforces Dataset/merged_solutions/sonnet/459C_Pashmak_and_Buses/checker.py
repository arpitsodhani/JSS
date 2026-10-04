"""459C accepts any seating where no two students share every day's bus."""


def check_for(stdin, expected):
    n, k, d = (int(v) for v in stdin.split())
    possible = expected.strip() != "-1"

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows[0][0] == "-1", "printed a seating where none exists"
            return
        assert rows[0][0] != "-1", "a seating exists but -1 was printed"
        assert len(rows) == d, f"expected {d} days, got {len(rows)}"
        plan = []
        for row in rows:
            values = [int(v) for v in row]
            assert len(values) == n, f"expected {n} students per day"
            assert all(1 <= v <= k for v in values), "bus number out of range"
            plan.append(values)
        seen = set()
        for student in range(n):
            key = tuple(plan[day][student] for day in range(d))
            assert key not in seen, "two students ride together every day"
            seen.add(key)

    return check
