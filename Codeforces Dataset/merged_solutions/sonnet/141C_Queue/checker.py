"""141C accepts any queue and any heights that match everybody's memory.

The printed order is replayed: for each person the number of taller people
standing before them has to equal the number they remembered.
"""


def check_for(stdin, expected):
    data = stdin.split()
    n = int(data[0])
    wanted = {}
    for i in range(n):
        wanted[data[1 + 2 * i]] = int(data[2 + 2 * i])
    possible = expected.strip() != "-1"

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows and rows[0][0] == "-1", "printed a queue where none exists"
            return
        assert rows[0][0] != "-1", "a queue exists but -1 was printed"
        assert len(rows) == n, f"expected {n} people, got {len(rows)}"
        names = [row[0] for row in rows]
        heights = [int(row[1]) for row in rows]
        assert sorted(names) == sorted(wanted), "the names differ from the input"
        for i in range(n):
            assert 1 <= heights[i] <= 10 ** 9, f"height {heights[i]} out of range"
            taller = sum(1 for j in range(i) if heights[j] > heights[i])
            assert taller == wanted[names[i]], \
                f"{names[i]} sees {taller} taller people, remembered {wanted[names[i]]}"

    return check
