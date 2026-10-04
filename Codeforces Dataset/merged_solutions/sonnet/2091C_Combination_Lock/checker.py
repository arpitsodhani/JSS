"""2091C accepts any permutation whose every cyclic shift has exactly one fixed
point; such a permutation exists exactly for odd n.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    sizes = data[1:1 + data[0]]

    def check(out):
        tokens = out.split()
        at = 0
        for n in sizes:
            if n % 2 == 0:
                assert tokens[at] == "-1", f"n={n}: expected -1, got {tokens[at]!r}"
                at += 1
                continue
            perm = [int(v) for v in tokens[at:at + n]]
            at += n
            assert sorted(perm) == list(range(1, n + 1)), f"n={n}: not a permutation"
            offsets = set()
            for i in range(n):
                offsets.add((perm[i] - (i + 1)) % n)
            assert len(offsets) == n, (
                f"n={n}: some cyclic shift has zero or several fixed points")
        assert at == len(tokens), "extra output"

    return check
