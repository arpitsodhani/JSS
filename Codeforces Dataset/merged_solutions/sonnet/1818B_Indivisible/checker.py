"""1818B accepts any permutation whose every window of length >= 2 has a sum not
divisible by the window length; only n = 1 and even n are solvable.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    sizes = data[1:1 + data[0]]

    def check(out):
        tokens = out.split()
        at = 0
        for n in sizes:
            possible = n == 1 or n % 2 == 0
            if not possible:
                assert tokens[at] == "-1", f"n={n}: expected -1, got {tokens[at]!r}"
                at += 1
                continue
            perm = [int(v) for v in tokens[at:at + n]]
            at += n
            assert sorted(perm) == list(range(1, n + 1)), f"n={n}: not a permutation"
            prefix = [0] * (n + 1)
            for i, value in enumerate(perm):
                prefix[i + 1] = prefix[i] + value
            for l in range(n):
                for r in range(l + 1, n):
                    width = r - l + 1
                    assert (prefix[r + 1] - prefix[l]) % width != 0, (
                        f"n={n}: window [{l+1}, {r+1}] divides")
        assert at == len(tokens), "extra output"

    return check
