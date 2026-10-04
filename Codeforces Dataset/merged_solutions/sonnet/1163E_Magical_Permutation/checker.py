"""1163E accepts any longest magical permutation.

The largest x is the biggest value for which the S elements below 2^x span a
space of dimension x over GF(2); the listing must then be a permutation of
0..2^x-1 whose consecutive xors all lie in S.
"""


def check_for(stdin, expected):
    tokens = [int(v) for v in stdin.split()]
    values = set(tokens[1:1 + tokens[0]])

    def rank_below(limit):
        basis = []
        for v in sorted(values):
            if v >= limit:
                break
            cur = v
            for b in basis:
                cur = min(cur, cur ^ b)
            if cur:
                basis.append(cur)
                basis.sort(reverse=True)
        return len(basis)

    best_x = 0
    for x in range(0, 20):
        if rank_below(1 << x) == x:
            best_x = x

    def check(out):
        got = [int(v) for v in out.split()]
        x = got[0]
        assert x == best_x, f"reported x={x}, the largest is {best_x}"
        seq = got[1:]
        assert len(seq) == (1 << x), f"expected {1 << x} numbers, got {len(seq)}"
        assert sorted(seq) == list(range(1 << x)), "not a permutation of 0..2^x-1"
        for i in range(len(seq) - 1):
            assert (seq[i] ^ seq[i + 1]) in values, (
                f"{seq[i]} xor {seq[i + 1]} = {seq[i] ^ seq[i + 1]} is not in S")

    return check
