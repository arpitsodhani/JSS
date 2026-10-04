"""1758D accepts any sequence of n distinct values in [1, 1e9] whose range equals
the square root of its sum."""


def check_for(stdin, expected):
    sizes = [int(v) for v in stdin.split()[1:]]

    def check(out):
        got = [int(v) for v in out.split()]
        at = 0
        for n in sizes:
            values = got[at:at + n]
            at += n
            assert len(values) == n, f"n={n}: expected {n} values"
            assert len(set(values)) == n, f"n={n}: values are not distinct"
            for v in values:
                assert 1 <= v <= 10 ** 9, f"n={n}: {v} outside [1, 1e9]"
            span = max(values) - min(values)
            assert span * span == sum(values), (
                f"n={n}: range {span} squared is {span * span}, sum is {sum(values)}")
        assert at == len(got), "trailing output"

    return check
