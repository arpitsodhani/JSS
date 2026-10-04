"""1722G accepts any array of distinct values with matching odd/even xors."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    sizes = data[1:1 + data[0]]

    def check(out):
        rows = [line.split() for line in out.split("\n") if line.strip()]
        assert len(rows) == len(sizes), f"expected {len(sizes)} lines, got {len(rows)}"
        for case in range(len(sizes)):
            values = [int(v) for v in rows[case]]
            n = sizes[case]
            assert len(values) == n, f"case {case + 1}: expected {n} values"
            assert len(set(values)) == n, f"case {case + 1}: values are not distinct"
            assert all(0 <= v < (1 << 31) for v in values), f"case {case + 1}: value out of range"
            even = 0
            odd = 0
            for i in range(n):
                if i % 2:
                    odd ^= values[i]
                else:
                    even ^= values[i]
            assert even == odd, f"case {case + 1}: xors differ ({even} vs {odd})"

    return check
