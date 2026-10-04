"""1264A accepts any maximal award split, so check the rules and the total.

Gold has to be the whole first block of equal scores (any larger prefix only
wastes medals), silver the fewest further blocks that beat it, and bronze as many
blocks as the half-of-all-participants cap allows; that maximises g+s+b.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    cases = []
    pos = 1
    for _ in range(int(tokens[0])):
        n = int(tokens[pos])
        pos += 1
        scores = [int(v) for v in tokens[pos:pos + n]]
        pos += n
        cases.append((n, scores))

    def blocks_of(scores):
        sizes = []
        run = 1
        for i in range(1, len(scores)):
            if scores[i] == scores[i - 1]:
                run += 1
            else:
                sizes.append(run)
                run = 1
        sizes.append(run)
        return sizes

    def reference(n, scores):
        sizes = blocks_of(scores)
        limit = n // 2
        gold = sizes[0]
        i = 1
        silver = 0
        while i < len(sizes) and silver <= gold:
            silver += sizes[i]
            i += 1
        if silver <= gold:
            return 0
        bronze = 0
        while i < len(sizes) and gold + silver + bronze + sizes[i] <= limit:
            bronze += sizes[i]
            i += 1
        if bronze <= gold or gold + silver + bronze > limit:
            return 0
        return gold + silver + bronze

    def check(out):
        got = [int(v) for v in out.split()]
        assert len(got) == 3 * len(cases), f"expected {3 * len(cases)} numbers, got {len(got)}"
        for case_no, (n, scores) in enumerate(cases, start=1):
            g, s, b = got[3 * (case_no - 1):3 * case_no]
            want = reference(n, scores)
            if want == 0:
                assert (g, s, b) == (0, 0, 0), f"case {case_no}: awarded {g} {s} {b}, none is possible"
                continue
            assert g + s + b == want, f"case {case_no}: awarded {g + s + b}, the maximum is {want}"
            assert g > 0 and s > 0 and b > 0, f"case {case_no}: every medal must be awarded"
            assert g < s and g < b, f"case {case_no}: gold {g} must be fewer than silver {s} and bronze {b}"
            assert g + s + b <= n // 2, f"case {case_no}: {g + s + b} medallists exceeds {n // 2}"
            for cut in (g, g + s, g + s + b):
                assert cut >= len(scores) or scores[cut - 1] > scores[cut], (
                    f"case {case_no}: the boundary at {cut} splits a group of equal scores")

    return check
