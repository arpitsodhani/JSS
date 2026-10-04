"""45D accepts any assignment of distinct days respecting every window."""


def check_for(stdin, expected):
    tokens = stdin.split()
    n = int(tokens[0])
    windows = [(int(tokens[1 + 2 * i]), int(tokens[2 + 2 * i])) for i in range(n)]

    def check(out):
        got = [int(x) for x in out.split()]
        assert len(got) == n, f"expected {n} dates, got {len(got)}"
        assert len(set(got)) == n, "two events share a day"
        for i, (day, (lo, hi)) in enumerate(zip(got, windows), start=1):
            assert lo <= day <= hi, f"event {i}: day {day} outside [{lo}, {hi}]"

    return check
