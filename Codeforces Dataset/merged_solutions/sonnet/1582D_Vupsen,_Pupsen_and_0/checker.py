"""1582D accepts any non-zero b with sum(a_i * b_i) == 0 and bounded absolute sum."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n

    def check(out):
        rows = [line for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            a = cases[case]
            b = [int(v) for v in rows[case].split()]
            assert len(b) == len(a), f"case {case + 1}: expected {len(a)} numbers"
            assert all(v != 0 for v in b), f"case {case + 1}: b contains a zero"
            assert sum(abs(v) for v in b) <= 10 ** 9, f"case {case + 1}: |b| sum too large"
            total = sum(a[i] * b[i] for i in range(len(a)))
            assert total == 0, f"case {case + 1}: dot product is {total}"

    return check
