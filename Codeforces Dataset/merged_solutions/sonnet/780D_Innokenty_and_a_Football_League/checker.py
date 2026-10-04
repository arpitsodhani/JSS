"""780D accepts any assignment of distinct three-letter short names.

Each club's name has to be one of its two allowed forms, and the second form is
only allowed for a club when no club could claim the same first form.
"""


def check_for(stdin, expected):
    data = stdin.split()
    n = int(data[0])
    clubs = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]
    possible = expected.strip().split("\n")[0].strip().upper() == "YES"

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows[0].upper() == "NO", "printed names where none exist"
            return
        assert rows[0].upper() == "YES", "an assignment exists but NO was printed"
        names = rows[1:1 + n]
        assert len(names) == n, f"expected {n} names, got {len(names)}"
        assert len(set(names)) == n, "two clubs share a short name"
        chosen_first = set()
        for i in range(n):
            team, town = clubs[i]
            first = team[:3]
            second = team[:2] + town[0]
            assert names[i] in (first, second), f"club {i + 1}: {names[i]} is not allowed"
            if names[i] == first:
                chosen_first.add(first)
        for i in range(n):
            team, town = clubs[i]
            first = team[:3]
            second = team[:2] + town[0]
            if names[i] == second and second != first:
                assert first not in chosen_first, \
                    f"club {i + 1} took its second form while {first} is used as a first form"

    return check
