"""2032B accepts any split into an odd number of odd-length subarrays whose
medians have median k.

Only n = 1 with k = 1, or 1 < k < n, admit a split, which the checker recomputes
before validating the printed starting positions.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    cases = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(t)]

    def check(out):
        tokens = out.split()
        at = 0
        for n, k in cases:
            possible = (n == 1 and k == 1) or (1 < k < n)
            if not possible:
                assert tokens[at] == "-1", f"n={n} k={k}: expected -1, got {tokens[at]!r}"
                at += 1
                continue
            m = int(tokens[at])
            at += 1
            assert m >= 1 and m % 2 == 1 and m <= n, f"n={n} k={k}: bad m={m}"
            starts = [int(v) for v in tokens[at:at + m]]
            at += m
            assert starts[0] == 1, f"first subarray must start at 1, got {starts[0]}"
            assert all(starts[i] < starts[i + 1] for i in range(m - 1)), "starts not increasing"
            assert starts[-1] <= n, "start beyond n"
            medians = []
            for i in range(m):
                left = starts[i]
                right = (starts[i + 1] - 1) if i + 1 < m else n
                size = right - left + 1
                assert size % 2 == 1, f"subarray [{left}, {right}] has even length"
                medians.append(left + size // 2)
            medians.sort()
            assert medians[m // 2] == k, (
                f"n={n} k={k}: median of medians is {medians[m // 2]}")
        assert at == len(tokens), "extra output"

    return check
