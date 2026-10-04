"""753A accepts any set of distinct positive numbers summing to n, of maximal size.

The maximal size is the largest k with k(k+1)/2 <= n, so the checker recomputes
that bound and then validates distinctness and the total.
"""


def check_for(stdin, expected):
    n = int(stdin.split()[0])
    best = 0
    while (best + 1) * (best + 2) // 2 <= n:
        best += 1

    def check(out):
        lines = [line for line in out.strip().splitlines() if line.strip()]
        assert len(lines) == 2, f"expected two lines, got {len(lines)}"
        k = int(lines[0])
        gifts = [int(v) for v in lines[1].split()]
        assert k == best, f"printed {k} children, the maximum is {best}"
        assert len(gifts) == k, f"line 2 has {len(gifts)} numbers, expected {k}"
        assert all(v >= 1 for v in gifts), "every child needs a positive number of candies"
        assert len(set(gifts)) == k, "the numbers must be distinct"
        assert sum(gifts) == n, f"the numbers sum to {sum(gifts)}, expected {n}"

    return check
