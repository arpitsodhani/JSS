"""1485D accepts any matrix of multiples whose neighbours differ by a fourth power.

The checker tests the three stated conditions directly.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, m = data[0], data[1]
    a = []
    pos = 2
    for _ in range(n):
        a.append(data[pos:pos + m])
        pos += m

    def is_fourth_power(value):
        if value <= 0:
            return False
        root = int(round(value ** 0.25))
        for k in (root - 1, root, root + 1):
            if k >= 1 and k ** 4 == value:
                return True
        return False

    def check(out):
        values = [int(v) for v in out.split()]
        assert len(values) == n * m, f"expected {n * m} numbers, got {len(values)}"
        b = [values[i * m:(i + 1) * m] for i in range(n)]
        for i in range(n):
            for j in range(m):
                assert 1 <= b[i][j] <= 10 ** 6, f"b[{i}][{j}]={b[i][j]} out of range"
                assert b[i][j] % a[i][j] == 0, (
                    f"b[{i}][{j}]={b[i][j]} is not a multiple of {a[i][j]}")
        for i in range(n):
            for j in range(m):
                if i + 1 < n:
                    assert is_fourth_power(abs(b[i][j] - b[i + 1][j])), (
                        f"vertical gap at ({i}, {j}) is not a fourth power")
                if j + 1 < m:
                    assert is_fourth_power(abs(b[i][j] - b[i][j + 1])), (
                        f"horizontal gap at ({i}, {j}) is not a fourth power")

    return check
