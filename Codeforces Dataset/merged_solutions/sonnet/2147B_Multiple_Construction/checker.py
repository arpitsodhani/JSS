"""2147B accepts any arrangement, so the printed array is checked directly.

Each value from 1 to n has to appear twice with its two positions a multiple of
that value apart.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    sizes = data[1:1 + data[0]]

    def check(out):
        numbers = [int(v) for v in out.split()]
        at = 0
        for n in sizes:
            row = numbers[at:at + 2 * n]
            at += 2 * n
            spots = {}
            for i in range(2 * n):
                spots.setdefault(row[i], []).append(i)
            assert sorted(spots) == list(range(1, n + 1)), f"n={n}: values are not 1..{n}"
            for value in spots:
                places = spots[value]
                assert len(places) == 2, f"n={n}: value {value} appears {len(places)} times"
                gap = places[1] - places[0]
                assert gap % value == 0, f"n={n}: value {value} sits {gap} apart"

    return check
