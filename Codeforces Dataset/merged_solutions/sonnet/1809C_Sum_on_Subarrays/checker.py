"""1809C accepts any array in [-1000, 1000] with exactly k positive-sum subarrays."""


def check_for(stdin, expected):
    tokens = [int(v) for v in stdin.split()]
    cases = []
    pos = 1
    for _ in range(tokens[0]):
        cases.append((tokens[pos], tokens[pos + 1]))
        pos += 2

    def check(out):
        got = [int(v) for v in out.split()]
        at = 0
        for n, k in cases:
            values = got[at:at + n]
            at += n
            assert len(values) == n, f"n={n}: expected {n} values"
            for v in values:
                assert -1000 <= v <= 1000, f"{v} outside [-1000, 1000]"
            positive = 0
            for i in range(n):
                running = 0
                for j in range(i, n):
                    running += values[j]
                    if running > 0:
                        positive += 1
            assert positive == k, f"n={n}: {positive} positive subarrays, wanted {k}"
        assert at == len(got), "trailing output"

    return check
