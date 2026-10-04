"""31A accepts any triple of distinct forms with a_i = a_j + a_k."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    a = data[1:1 + data[0]]
    possible = expected.strip() != "-1"

    def check(out):
        parts = out.split()
        if not possible:
            assert parts[0] == "-1", "printed a triple where none exists"
            return
        assert parts[0] != "-1", "a triple exists but -1 was printed"
        i, j, k = (int(v) for v in parts[:3])
        assert len({i, j, k}) == 3, "the three forms must be distinct"
        assert all(1 <= v <= len(a) for v in (i, j, k)), "index out of range"
        assert a[i - 1] == a[j - 1] + a[k - 1], "the lengths do not add up"

    return check
