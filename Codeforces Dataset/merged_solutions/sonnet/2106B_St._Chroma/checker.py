"""2106B accepts any permutation maximising the number of cells painted x.

MEX reaches x only once 0..x-1 have all appeared and x has not, so the best is
to lead with 0..x-1, follow with everything above x, and leave x for last. That
paints cells x..n-1, i.e. n-x of them; x=0 has no lead-in so it paints n-1; and
x=n can only be reached by the final cell, so exactly 1.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    cases = []
    pos = 1
    for _ in range(int(tokens[0])):
        cases.append((int(tokens[pos]), int(tokens[pos + 1])))
        pos += 2

    def best(n, x):
        if x == n:
            return 1
        if x == 0:
            return n - 1
        return n - x

    def check(out):
        got = out.split()
        at = 0
        for case_no, (n, x) in enumerate(cases, start=1):
            p = [int(v) for v in got[at:at + n]]
            at += n
            assert len(p) == n, f"case {case_no}: expected {n} values"
            assert sorted(p) == list(range(n)), f"case {case_no}: not a permutation of 0..{n - 1}"
            seen = [False] * (n + 2)
            mex = 0
            painted = 0
            for value in p:
                seen[value] = True
                while mex <= n and seen[mex]:
                    mex += 1
                if mex == x:
                    painted += 1
            assert painted == best(n, x), (
                f"case {case_no} (n={n}, x={x}): painted {painted} cells, the best is {best(n, x)}")
        assert at == len(got), "trailing output"

    return check
