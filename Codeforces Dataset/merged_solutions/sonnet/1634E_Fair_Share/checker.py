"""1634E accepts any split in which every array contributes half its elements to
each side and the two multisets match.

A split exists exactly when every value occurs an even number of times overall,
which the checker recomputes before validating the printed letters.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    m = data[0]
    pos = 1
    arrays = []
    for _ in range(m):
        n = data[pos]
        pos += 1
        arrays.append(data[pos:pos + n])
        pos += n
    tally = {}
    for row in arrays:
        for value in row:
            tally[value] = tally.get(value, 0) + 1
    possible = all(count % 2 == 0 for count in tally.values())

    def check(out):
        lines = out.split()
        if not possible:
            assert lines[0].upper() == "NO", f"no split exists, printed {lines[0]!r}"
            return
        assert lines[0].upper() == "YES", f"a split exists, printed {lines[0]!r}"
        assert len(lines) == m + 1, f"expected {m} lines of letters, got {len(lines) - 1}"
        left = {}
        right = {}
        for row, letters in zip(arrays, lines[1:]):
            assert len(letters) == len(row), f"row length {len(letters)} != {len(row)}"
            assert set(letters) <= set("LR"), f"bad letters {letters!r}"
            assert letters.count("L") * 2 == len(row), (
                f"row has {letters.count('L')} L of {len(row)}")
            for value, side in zip(row, letters):
                bucket = left if side == "L" else right
                bucket[value] = bucket.get(value, 0) + 1
        assert left == right, "the two multisets differ"

    return check
